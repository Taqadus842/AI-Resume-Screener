export default function SkillList({ skills }) {
  return (
    <div className="bg-white shadow-lg rounded-xl p-6 mt-6">
      <h2 className="text-2xl font-bold mb-4">
        Missing Skills
      </h2>

      <ul className="list-disc list-inside space-y-2">
        {skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}