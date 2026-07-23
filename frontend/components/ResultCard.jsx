export default function ResultCard({ suggestions }) {
  return (
    <div className="bg-white shadow-lg rounded-xl p-6 mt-6">
      <h2 className="text-2xl font-bold mb-4">
        AI Suggestions
      </h2>

      <ul className="list-disc list-inside space-y-2">
        {suggestions.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}