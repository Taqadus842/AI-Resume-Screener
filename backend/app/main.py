from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import analyze, resume

app = FastAPI(
    title="AI Resume Screener API",
    description="Backend API for uploading resumes and analyzing them against job descriptions.",
    version="1.0.0",
)

# Allow the Next.js frontend (localhost:3000) to call this API during development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)
app.include_router(analyze.router)


@app.get("/")
async def root():
    return {"status": "ok", "message": "AI Resume Screener API is running."}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
