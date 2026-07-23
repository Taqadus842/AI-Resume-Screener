export default function ScoreCard({ score }) {
  return (
    <div className="bg-white shadow-lg rounded-xl p-6 text-center">
      <h2 className="text-2xl font-bold mb-4">
        Match Score
      </h2>

      <p className="text-6xl font-bold text-green-600">
        {score}%
      </p>
    </div>
  );
}