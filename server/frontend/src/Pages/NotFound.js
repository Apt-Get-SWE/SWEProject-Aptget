import { useNavigate } from "react-router-dom";

const NotFound = () => {
  const navigate = useNavigate();
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center items-center">
      <div className="max-w-lg w-full">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Page not found</h1>
        <p className="text-gray-700 text-lg mb-8">Oops! The page you are looking for does not exist.</p>
        <button className="px-6 py-3 bg-green-600 text-white font-bold rounded hover:bg-indigo-500 transition duration-200" onClick={() => {navigate("/dashboard")}}>
          Go back home
        </button>
      </div>
    </div>
  );
};

export default NotFound;
