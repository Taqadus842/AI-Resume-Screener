import Navbar from "@/components/Navbar";
import UploadForm from "@/components/UploadForm";

export default function UploadPage() {
  return (
    <>
      <Navbar />

      <main className="min-h-screen bg-gray-100 py-16 px-6">
        <UploadForm />
      </main>
    </>
  );
}