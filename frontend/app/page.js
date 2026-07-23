import Navbar from "@/components/Navbar";
import Link from "next/link";

export default function Home() {
  return (
    <>
      <Navbar />

      <main className="min-h-screen bg-gray-100">

        {/* Hero Section */}

        <section className="text-center py-20 px-6">

          <h1 className="text-5xl font-bold text-blue-700 mb-6">
            AI Resume Screener
          </h1>

          <p className="text-lg text-gray-700 max-w-3xl mx-auto mb-8">
            Upload your resume and compare it with your dream job description
            using Artificial Intelligence. Receive a match score, identify
            missing skills, and get smart suggestions to improve your resume.
          </p>

         <Link href="/upload">
  <button className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition">
    Analyze Resume
  </button>
</Link>
        </section>

        {/* Key Features */}

        <section className="max-w-6xl mx-auto px-6 py-16">

          <h2 className="text-3xl font-bold text-center mb-10">
            Key Features
          </h2>

          <div className="grid md:grid-cols-2 gap-8">

            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-3">
                Resume Analysis
              </h3>

              <p>
                Compare resumes against job descriptions using AI.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-3">
                Match Score
              </h3>

              <p>
                Receive an AI-generated compatibility score from 0 to 100.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-3">
                Missing Skills
              </h3>

              <p>
                Discover important skills missing from your resume.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-3">
                AI Suggestions
              </h3>

              <p>
                Get personalized recommendations to improve your resume.
              </p>
            </div>

          </div>

        </section>

        {/* Benefits */}

        <section className="bg-blue-50 py-16 px-6">

          <h2 className="text-3xl font-bold text-center mb-8">
            Why Use AI Resume Screener?
          </h2>

          <ul className="max-w-3xl mx-auto space-y-4 text-lg">

            <li>✅ Save time while reviewing resumes.</li>

            <li>✅ Improve your ATS compatibility.</li>

            <li>✅ Get instant AI-powered feedback.</li>

            <li>✅ Increase your chances of getting interviews.</li>

          </ul>

        </section>

      </main>
    </>
  );
}