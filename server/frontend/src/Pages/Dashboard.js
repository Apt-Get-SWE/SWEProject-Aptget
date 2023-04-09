import React, { useState } from 'react';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import ItemCard from '../Components/ItemCard/ItemCard'; // Make sure to import ItemCard

const Dashboard = () => {
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();

    // Collect form data
    const formData = new FormData(event.target);

    // TODO: Call the Flask API endpoint to post the item to the backend database

    // Close the modal
    setShowModal(false);
  };

  return (
    <div className="min-h-screen">
      <Navbar />
      <div className="w-5/6 mx-auto">
        <button
          className="w-full max-w-sm bg-blue-700 hover:bg-blue-800 text-white rounded-lg shadow mt-5 h-[216px] flex items-center justify-center"
          onClick={() => setShowModal(true)}
        >
          Add New Item
        </button>

        {showModal && (
          <>
            <div
              className="fixed inset-0 bg-black opacity-50 z-10"
              onClick={() => setShowModal(false)}
            ></div>
            <div className="fixed inset-0 flex items-center justify-center z-20">
              <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md w-3/4 mx-auto my-10 p-8">
                <h2 className="text-2xl mb-4">Add New Item</h2>
                <form onSubmit={handleSubmit}>
                  <label htmlFor="title" className="block mb-1">
                    Title:
                  </label>
                  <input
                    type="text"
                    id="title"
                    name="title"
                    className="w-full mb-4 p-1 border border-gray-300 rounded"
                    required
                  />

                  <label htmlFor="condition" className="block mb-1">
                    Condition:
                  </label>
                  <input
                    type="text"
                    id="condition"
                    name="condition"
                    className="w-full mb-4 p-1 border border-gray-300 rounded"
                    required
                  />

                  <label htmlFor="price" className="block mb-1">
                    Price:
                  </label>
                  <input
                    type="number"
                    id="price"
                    name="price"
                    className="w-full mb-4 p-1 border border-gray-300 rounded"
                    required
                  />

                  <label htmlFor="status" className="block mb-1">
                    Sold Status:
                  </label>
                  <select
                    id="status"
                    name="status"
                    className="w-full mb-4 p-1 border border-gray-300 rounded"
                    required
                  >
                    <option value="Sold">Sold</option>
                    <option value="Available">Available</option>
                    <option value="Pending">Pending</option>
                  </select>

                  <label htmlFor="description" className="block mb-1">
                    Description:
                  </label>
                  <textarea
                    id="description"
                    name="description"
                    className="w-full mb-4 p-1 border border-gray-300 rounded"
                    rows="4"
                    required
                  ></textarea>

                  <button
                    type="submit"
                    className="bg-blue-700 hover:bg-blue-800 text-white rounded-lg px-4 py-2 mr-2"
                  > 
                  Submit
                  </button>
                  <button
                  type="button"
                  className="bg-red-500 hover:bg-red-600 text-white rounded-lg px-4 py-2"
                  onClick={() => setShowModal(false)}
                  >
                  Cancel
                  </button>
                </form>
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