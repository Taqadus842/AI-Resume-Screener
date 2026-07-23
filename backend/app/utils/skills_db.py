"""
A curated database of common skills / technologies / tools used to detect
skill keywords inside a job description and a resume.

This is intentionally a plain Python list so it can be extended easily
without touching any other part of the codebase.
"""

SKILLS_DB = [
    # Programming languages
    "python", "java", "javascript", "typescript", "c++", "c#", "c",
    "go", "golang", "rust", "ruby", "php", "swift", "kotlin", "scala",
    "r", "matlab", "perl", "dart", "objective-c", "sql", "bash", "shell",

    # Web / frontend
    "html", "css", "sass", "less", "react", "react.js", "next.js", "nextjs",
    "vue", "vue.js", "angular", "angular.js", "svelte", "tailwind",
    "tailwindcss", "bootstrap", "jquery", "redux", "webpack", "vite",
    "graphql", "rest", "rest api", "restful api", "websocket",

    # Backend / frameworks
    "node.js", "nodejs", "express", "express.js", "django", "flask",
    "fastapi", "spring", "spring boot", "asp.net", ".net", "laravel",
    "ruby on rails", "rails", "nestjs",

    # Databases
    "mysql", "postgresql", "postgres", "mongodb", "sqlite", "redis",
    "oracle", "sql server", "dynamodb", "cassandra", "firebase",
    "elasticsearch", "neo4j",

    # Cloud / devops
    "aws", "amazon web services", "azure", "gcp", "google cloud",
    "docker", "kubernetes", "k8s", "terraform", "ansible", "jenkins",
    "ci/cd", "cicd", "github actions", "gitlab ci", "linux", "unix",
    "nginx", "apache", "microservices", "serverless", "cloudformation",

    # Data / AI / ML
    "machine learning", "deep learning", "artificial intelligence",
    "data science", "data analysis", "data engineering", "nlp",
    "natural language processing", "computer vision", "tensorflow",
    "pytorch", "keras", "scikit-learn", "sklearn", "pandas", "numpy",
    "matplotlib", "power bi", "tableau", "excel", "big data", "spark",
    "hadoop", "etl", "data visualization", "statistics", "opencv",
    "generative ai", "llm", "large language models", "chatgpt",

    # Tools / practices
    "git", "github", "gitlab", "bitbucket", "jira", "confluence",
    "agile", "scrum", "kanban", "unit testing", "test driven development",
    "tdd", "postman", "swagger", "figma", "photoshop", "illustrator",
    "ui/ux", "ux design", "ui design", "wireframing",

    # Mobile
    "android", "ios", "react native", "flutter", "xamarin",

    # Soft skills
    "communication", "leadership", "teamwork", "problem solving",
    "critical thinking", "time management", "project management",
    "collaboration", "adaptability", "creativity", "attention to detail",
    "analytical skills", "presentation skills", "negotiation",
    "customer service", "mentoring", "public speaking",

    # Security
    "cybersecurity", "penetration testing", "network security",
    "information security", "encryption", "vulnerability assessment",

    # Misc business
    "seo", "digital marketing", "content marketing", "salesforce",
    "sap", "erp", "crm", "accounting", "finance", "budgeting",
    "product management", "business analysis", "stakeholder management",
]

# De-duplicate while preserving order and normalize to lowercase
SKILLS_DB = sorted(set(s.lower() for s in SKILLS_DB), key=len, reverse=True)

# A small set of generic English stopwords used when extracting
# extra candidate keywords that are not in SKILLS_DB (e.g. domain
# specific nouns mentioned in the job description).
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "so", "of", "to",
    "in", "on", "for", "with", "as", "by", "at", "from", "is", "are",
    "was", "were", "be", "been", "being", "this", "that", "these",
    "those", "it", "its", "you", "your", "we", "our", "they", "their",
    "will", "would", "should", "can", "could", "may", "might", "must",
    "have", "has", "had", "do", "does", "did", "not", "no", "yes",
    "job", "role", "work", "working", "years", "year", "experience",
    "team", "including", "such", "etc", "using", "use", "used", "who",
    "what", "when", "where", "why", "how", "all", "any", "each", "more",
    "most", "other", "some", "than", "too", "very", "just", "about",
    "into", "through", "during", "before", "after", "above", "below",
    "up", "down", "out", "off", "over", "under", "again", "further",
    "once", "here", "there", "both", "each", "few", "same", "own",
    "strong", "looking", "senior", "junior", "ideal", "candidate",
    "candidates", "familiarity", "big", "plus", "bonus", "required",
    "requirements", "responsibilities", "preferred", "ability", "abilities",
    "skills", "skill", "knowledge", "proficient", "proficiency", "solid",
    "excellent", "good", "great", "new", "join", "join us", "company",
    "opportunity", "environment", "position", "successful", "self",
    "highly", "must", "plus.", "including", "you'll", "we're", "they're",
}
