"""
Core analysis engine.

Computes:
  - match_score: how well the resume matches the job description (0-100)
  - missing_keywords: important skills/keywords present in the job
    description but missing from the resume
  - suggestions: actionable, human readable suggestions to improve the resume
"""

import re
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.utils.skills_db import SKILLS_DB, STOPWORDS

WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z\+\.#\-]*")


def _normalize(text: str) -> str:
    return text.lower()


def _tfidf_similarity(resume_text: str, job_description: str) -> float:
    """
    Returns a 0-100 similarity score between the resume and the job
    description using TF-IDF weighted cosine similarity.
    """
    documents = [resume_text, job_description]
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(documents)
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    except ValueError:
        # Happens if the vocabulary is empty after removing stop words
        similarity = 0.0

    return round(float(similarity) * 100, 2)


def _find_known_skills(text: str) -> set:
    """
    Find every skill from SKILLS_DB that appears in `text` (case-insensitive,
    whole-word / whole-phrase match).
    """
    normalized = _normalize(text)
    found = set()
    for skill in SKILLS_DB:
        # Build a regex that matches the skill as a whole word/phrase,
        # allowing for the punctuation that can appear inside skill names
        # (e.g. "c++", "node.js").
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, normalized):
            found.add(skill)
    return found


def _extract_candidate_keywords(text: str, top_n: int = 15) -> list:
    """
    Extract additional candidate keywords from the job description that
    are not part of the curated SKILLS_DB, based on word frequency.
    Useful for domain-specific terms the curated list doesn't cover.

    Words are required to appear more than once, which filters out most
    generic adjectives/nouns ("strong", "senior", "looking") while still
    surfacing recurring domain-specific terms.
    """
    raw_words = WORD_RE.findall(text)
    words = []
    for w in raw_words:
        w = w.lower().strip(".-#+")  # strip stray trailing/leading punctuation
        if len(w) > 2 and w not in STOPWORDS and not w.isdigit():
            words.append(w)

    freq = Counter(words)
    # Only keep words that repeat, or are otherwise notably long (likely
    # a meaningful domain term rather than filler language).
    candidates = [w for w, c in freq.items() if c >= 2 or len(w) >= 9]
    candidates.sort(key=lambda w: (-freq[w], w))
    return candidates[:top_n]


def _keyword_overlap_score(resume_skills: set, jd_skills: set) -> float:
    if not jd_skills:
        return 100.0
    matched = resume_skills & jd_skills
    return round((len(matched) / len(jd_skills)) * 100, 2)


def _build_suggestions(
    match_score: float,
    missing_keywords: list,
    resume_text: str,
    job_description: str,
) -> list:
    suggestions = []

    # Score based feedback
    if match_score >= 80:
        suggestions.append(
            "Excellent match! Your resume aligns strongly with this job description. "
            "Do a final proofread and make sure your most relevant experience appears near the top."
        )
    elif match_score >= 60:
        suggestions.append(
            "Good match overall. Tailor a few bullet points to mirror the exact "
            "wording used in the job description to improve ATS keyword matching."
        )
    elif match_score >= 40:
        suggestions.append(
            "Moderate match. Consider rewriting your summary/objective section to "
            "closely reflect the role's key responsibilities and required skills."
        )
    else:
        suggestions.append(
            "Low match score. Your resume may need significant tailoring for this "
            "role — add relevant projects, skills, and experience that align with "
            "the job description."
        )

    # Missing keyword based feedback
    if missing_keywords:
        top_missing = missing_keywords[:8]
        suggestions.append(
            "Consider adding evidence of these skills/keywords if you have them: "
            + ", ".join(top_missing) + "."
        )
        suggestions.append(
            "If you have experience with any of the missing skills above, add a "
            "dedicated 'Skills' section or weave them naturally into your project "
            "and work experience bullet points."
        )
    else:
        suggestions.append(
            "Your resume already covers the key skills mentioned in the job description. Nice work!"
        )

    # Structural / general resume advice
    word_count = len(resume_text.split())
    if word_count < 150:
        suggestions.append(
            "Your resume looks quite short. Consider expanding on your work "
            "experience, projects, and achievements with quantifiable results."
        )
    elif word_count > 1200:
        suggestions.append(
            "Your resume is quite long. Consider trimming it down to 1-2 pages, "
            "keeping only the most relevant and recent experience."
        )

    if not re.search(r"\b\d+%|\b\d+\+|\$\d+", resume_text):
        suggestions.append(
            "Add quantifiable achievements (e.g. 'increased efficiency by 20%', "
            "'managed a team of 5') to make your impact more measurable."
        )

    return suggestions


def analyze_resume(resume_text: str, job_description: str) -> dict:
    resume_text = (resume_text or "").strip()
    job_description = (job_description or "").strip()

    # --- Similarity score (blend of TF-IDF cosine similarity and skill overlap) ---
    tfidf_score = _tfidf_similarity(resume_text, job_description)

    resume_skills = _find_known_skills(resume_text)
    jd_skills = _find_known_skills(job_description)
    overlap_score = _keyword_overlap_score(resume_skills, jd_skills)

    # Weighted blend: keyword overlap is a stronger, more interpretable
    # signal for resume/JD matching, TF-IDF captures general topical overlap.
    match_score = round((0.4 * tfidf_score) + (0.6 * overlap_score))
    match_score = max(0, min(100, match_score))

    # --- Missing keywords ---
    missing_skill_set = jd_skills - resume_skills

    # Supplement with high-frequency candidate keywords from the JD that
    # aren't in our curated skill list, in case they're missing from resume too.
    candidate_keywords = _extract_candidate_keywords(job_description)
    normalized_resume = _normalize(resume_text)
    extra_missing = [
        kw for kw in candidate_keywords
        if kw not in resume_skills
        and kw not in missing_skill_set
        and not re.search(r"(?<![a-zA-Z0-9])" + re.escape(kw) + r"(?![a-zA-Z0-9])", normalized_resume)
    ]

    missing_keywords = sorted(missing_skill_set) + extra_missing[:5]

    # --- Suggestions ---
    suggestions = _build_suggestions(match_score, missing_keywords, resume_text, job_description)

    return {
        "match_score": match_score,
        "missing_keywords": missing_keywords if missing_keywords else ["None — great coverage!"],
        "suggestions": suggestions,
        "matched_keywords": sorted(resume_skills & jd_skills),
    }
