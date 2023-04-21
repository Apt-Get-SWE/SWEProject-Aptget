import React, { useState } from 'react';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import ItemCard from '../Components/ItemCard/ItemCard';

const SearchBar = () => {
  const [zipcode, setZipcode] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Searching for zipcode:', zipcode);
    // Implement your search logic here
  };

  return (
    <form onSubmit={handleSubmit} className="w-full p-4 flex justify-center">
      <div className='flex'>
        <input
          type="text"
          placeholder="Enter zipcode"
          value={zipcode}
          onChange={(e) => setZipcode(e.target.value)}
          className="w-full px-4 py-2 pr-10 border border-green-400 rounded focus:outline-none focus:border-green-500"
        />
        <button type="submit" className="rounded-lg px-3 text-white bg-green-500 hover:bg-green-600 ml-4">Search</button>
      </div>
    </form>
  );
};

const Market = () => {
  return (
    <div className="min-h-screen">
      <Navbar />
      <SearchBar />
      <div className="grid grid-cols-3 gap-4 w-5/6 mx-auto">
        <div className="p-4">
          <ItemCard itemName="TestItem" />
        </div>
        <div className="p-4">
          <ItemCard itemName="TestItem" />
        </div>
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  );
};

export default Market;
