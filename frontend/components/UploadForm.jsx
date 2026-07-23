"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { uploadResume, analyzeResume } from "@/services/api";
export default function UploadForm() {
  const router = useRouter();

  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [error, setError] = useState("");
  const [fileInputKey, setFileInputKey] = useState(0);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
  e.preventDefault();

  if (!resume) {
    setError("Please select a resume.");
    return;
  }

  const allowedTypes = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  ];

  if (!allowedTypes.includes(resume.type)) {
    setError("Only PDF and DOCX files are allowed.");
    return;
  }

  if (jobDescription.trim() === "") {
    setError("Please enter a job description.");
    return;
  }

  try {
    setLoading(true);
    setError("");

    // Step 1: Upload Resume
    const uploadResult = await uploadResume(resume);

    // Step 2: Analyze Resume
    const analysisResult = await analyzeResume(
      uploadResult.resume_text,
      jobDescription
    );

    console.log("AI Response:", analysisResult);

    // Store result in localStorage
    localStorage.setItem("analysisResult", JSON.stringify(analysisResult));

    router.push("/results");

  } catch (err) {
  console.error(err);

  setError(
    err.message ||
    "Something went wrong."
  );
} finally {
    setLoading(false);
  }
};
  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow-lg rounded-xl p-8 max-w-2xl mx-auto"
    >
      <h2 className="text-3xl font-bold mb-6 text-center">
        Upload Resume
      </h2>

     <label className="block font-semibold mb-2">
  Choose Resume (PDF/DOCX)
  <span className="text-red-600 ml-1">*</span>
</label>

<input
  id="resume"
  key={fileInputKey}
  type="file"
  accept=".pdf,.docx"
  onChange={(e) => setResume(e.target.files[0])}
  className="hidden"
/>

<label
  htmlFor="resume"
  className="flex items-center justify-between border rounded-lg p-3 cursor-pointer hover:bg-gray-50 mb-6"
>
  <span className="text-gray-700">
    {resume ? `📄 ${resume.name}` : "Choose Resume"}
  </span>

  {resume && (
    <button
      type="button"
      onClick={(e) => {
        e.preventDefault();
        setResume(null);
        setFileInputKey(fileInputKey + 1);
      }}
      className="text-red-600 font-bold text-xl hover:text-red-800"
    >
      ✖
    </button>
  )}
</label>
      <textarea
        rows="8"
        placeholder="Paste Job Description Here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        className="w-full border p-3 rounded-lg mb-4"
      />

      {error && (
        <p className="text-red-600 mb-4 font-medium">
          {error}
        </p>
      )}

      <button
        type="submit"
        className="bg-blue-600 text-white px-6 py-3 rounded-lg w-full hover:bg-blue-700 transition"
      >
        Analyze Resume
      </button>
    </form>
  );
}