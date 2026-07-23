const BASE_URL = "http://127.0.0.1:8000";

export async function uploadResume(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${BASE_URL}/api/resume/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Resume upload failed.");
  }

  return await response.json();
}

export async function analyzeResume(resumeText, jobDescription) {
  const response = await fetch(`${BASE_URL}/api/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      resume_text: resumeText,
      job_description: jobDescription,
    }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || "Analysis failed.");
  }

  return await response.json();
}