import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def analyze_resume(
        resume_text,
        job_description
):

    prompt = f"""
You are an AI Resume Reviewer.

Compare the resume with job description.

Return ONLY JSON.

Format:

{{
"match_score": number,
"missing_keywords": [],
"suggestions": []
}}

Resume:

{resume_text}


Job Description:

{job_description}
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


    return response.text