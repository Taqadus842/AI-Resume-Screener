# AI Resume Screener — Backend

FastAPI backend for the AI Resume Screener. It parses uploaded resumes
(PDF/DOCX), compares them against a job description, and returns a match
score, missing keywords, and improvement suggestions.

No external AI API key is required — the analysis runs fully locally using
TF-IDF cosine similarity (scikit-learn) combined with a curated skills
database for keyword matching.

## Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000`.
Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`

## Endpoints

### `POST /api/resume/upload`
Multipart form upload. Field name: `file` (PDF or DOCX, max 10MB).

Response:
```json
{
  "filename": "resume.pdf",
  "resume_text": "extracted plain text...",
  "message": "Resume uploaded and parsed successfully."
}
```

### `POST /api/analyze`
JSON body:
```json
{
  "resume_text": "...",
  "job_description": "..."
}
```

Response:
```json
{
  "match_score": 72,
  "missing_keywords": ["kubernetes", "graphql"],
  "suggestions": ["...", "..."],
  "matched_keywords": ["python", "django"]
}
```

### `GET /health`
Simple health check, returns `{"status": "healthy"}`.

## Project structure

```
backend/
  app/
    main.py                 # FastAPI app, CORS, router registration
    routers/
      resume.py             # /api/resume/upload
      analyze.py             # /api/analyze
    services/
      parser.py             # PDF/DOCX text extraction
      analyzer.py           # match score, missing keywords, suggestions
    utils/
      skills_db.py          # curated skills list + stopwords
  requirements.txt
```

## Notes

- CORS is pre-configured to allow requests from `http://localhost:3000`
  (the Next.js frontend's default dev port).
- Max upload size is 10MB; only `.pdf` and `.docx` files are accepted.
- The match score blends TF-IDF cosine similarity (40%) with skill-keyword
  overlap (60%) between the resume and job description.
