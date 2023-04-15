import React, { useState } from 'react';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const [showModal, setShowModal] = useState(false);
  const navigate = useNavigate();

  return (
    <div className="min-h-screen">
      <Navbar />
      <div className="w-5/6 mx-auto">
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
          onClick={() => navigate('/create')}
        >
          Add New Item
        </button>
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  );
};

export default Dashboard;