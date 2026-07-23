"use client";

import { useEffect, useState } from "react";

import Navbar from "@/components/Navbar";
import ScoreCard from "@/components/ScoreCard";
import SkillList from "@/components/SkillList";
import ResultCard from "@/components/ResultCard";

export default function ResultsPage() {
  const [result, setResult] = useState(null);

  useEffect(() => {
    const data = localStorage.getItem("analysisResult");

    if (data) {
      setResult(JSON.parse(data));
    }
  }, []);

  if (!result) {
    return (
      <>
        <Navbar />
        <main className="min-h-screen flex justify-center items-center">
          <h2 className="text-2xl font-bold">
            No Analysis Result Found
          </h2>
        </main>
      </>
    );
  }

  return (
    <>
      <Navbar />

      <main className="min-h-screen bg-gray-100 py-10 px-6">
        <h1 className="text-4xl font-bold text-center mb-10">
          AI Resume Analysis Results
        </h1>

        <div className="max-w-4xl mx-auto">

          <ScoreCard score={result.match_score} />

          <SkillList skills={result.missing_keywords} />

          <ResultCard suggestions={result.suggestions} />

        </div>
      </main>
    </>
  );
}