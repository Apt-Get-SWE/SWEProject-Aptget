import React, { useState } from 'react';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import ItemInfoForm from '../Components/Forms/ItemInfoForm'; // Make sure to import ItemCard
import axios from 'axios';

const Dashboard = () => {
  const [showModal, setShowModal] = useState(false);

  const userPosts = async () => {
    // TODO get UID from user session
    const uid = 0;
    const res = await axios.get(`/api/posts/posts?uid=${uid}`);
    console.log(res.data)
    return res.data
  };

  return (
    <div className="min-h-screen">
      <Navbar />
      <div className="w-5/6 mx-auto" onMouseEnter={() => userPosts()}>
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
          onClick={() => setShowModal(true)}
        >
          Add New Item
        </button>
        {showModal && (
          <>
            <div
              className="fixed inset-0 bg-gray-900 bg-opacity-50 z-10"
              onClick={() => setShowModal(false)}
            ></div>
            <div className="fixed inset-0 flex items-center justify-center z-20">
              <div className="bg-white rounded-lg w-full max-w-lg p-6">
                <h2 className="text-xl font-bold mb-4">Add New Item</h2>
                <ItemInfoForm setTrigger={setShowModal} />
              </div>
            </div>
          </>
        )}
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  );
};

export default Dashboard;