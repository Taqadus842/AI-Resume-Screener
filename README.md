# AI Resume Screener — Full Stack Project

A complete, working full-stack application:
- **Frontend**: Next.js (App Router) + Tailwind CSS
- **Backend**: FastAPI (Python) — resume parsing + AI-style analysis, no external API key required

```
project/
  frontend/     # Next.js app (upload UI, results page)
  backend/      # FastAPI app (parsing + analysis engine)
```

## Quick start

### 1. Start the backend (port 8000)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 2. Start the frontend (port 3000)

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

### 3. Use it

Open [http://localhost:3000](http://localhost:3000), click **Analyze Resume**,
upload a PDF or DOCX resume, paste a job description, and submit. You'll be
taken to `/results` with your match score, missing keywords, and suggestions.

## How it works

1. The frontend uploads the resume file to `POST /api/resume/upload`.
   The backend extracts plain text from the PDF/DOCX using `pdfplumber` /
   `python-docx`.
2. The frontend sends the extracted text + job description to
   `POST /api/analyze`.
3. The backend:
   - Computes a **TF-IDF cosine similarity** score between the resume and
     job description (topical overlap).
   - Extracts known skills/technologies from both texts using a curated
     skills database and computes a **keyword overlap score**.
   - Blends both into a single 0–100 **match score**.
   - Returns the list of important keywords present in the job description
     but missing from the resume.
   - Generates human-readable **suggestions** based on the score, missing
     keywords, and general resume-quality heuristics (length, quantifiable
     achievements, etc).
4. Results are stored in `localStorage` and rendered on `/results`.

## Troubleshooting

- **"Failed to fetch" / network error on upload**: make sure the backend is
  running on `http://127.0.0.1:8000` (check `frontend/services/api.js` if you
  change the port).
- **CORS error in browser console**: the backend only allows
  `http://localhost:3000` and `http://127.0.0.1:3000` by default — update
  `backend/app/main.py`'s `CORSMiddleware` origins if you deploy elsewhere.
- **"No readable text found in the PDF"**: the uploaded PDF is likely a
  scanned image without a text layer. Use a text-based PDF or DOCX instead.
