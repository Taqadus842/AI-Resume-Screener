from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import resume, analysis


app = FastAPI(
    title="AI Resume Screener API",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    resume.router,
    prefix="/api/resume",
    tags=["Resume"]
)


app.include_router(
    analysis.router,
    prefix="/api",
    tags=["Analysis"]
)


@app.get("/")
def home():
    return {
        "message":"AI Resume Screener Backend Running"
    }