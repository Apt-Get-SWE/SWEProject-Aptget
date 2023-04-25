import React, { useState } from 'react';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import ItemCard from '../Components/ItemCard/ItemCard';
import axios from 'axios';

const SearchBar = ({ onSearch }) => {
  const [zipcode, setZipcode] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(zipcode);
  };

  return (
    <form onSubmit={handleSubmit} className="w-96 p-4 flex justify-center">
      <div className='flex'>
        <input
          type="text"
          placeholder="Enter zipcode"
          value={zipcode}
          onChange={(e) => setZipcode(e.target.value)}
          className="w-64 px-4 py-2 pr-10 border border-green-400 rounded focus:outline-none focus:border-green-500"
        />
        <button type="submit" className="rounded-lg px-3 text-white bg-green-500 hover:bg-green-600 ml-4">Search</button>
      </div>
    </form>
  );
};

const FilterBar = ({ onFilter }) => {
  const [filterText, setFilterText] = useState('');

  const handleChange = (e) => {
    setFilterText(e.target.value);
    onFilter(e.target.value);
  };

  return (
    <div className="w-96 p-4">
      <input
        type="text"
        placeholder="Filter results"
        value={filterText}
        onChange={handleChange}
        className="w-full px-4 py-2 pr-10 border border-green-400 rounded focus:outline-none focus:border-green-500"
      />
    </div>
  );
};

const Market = () => {
  const [items, setItems] = useState([]);
  const [filteredItems, setFilteredItems] = useState(items);
  const [searchPerformed, setSearchPerformed] = useState(false);

  const handleSearch = (zipcode) => {
    console.log('Searching for zipcode:', zipcode);
    try {
      const res = axios.get(`/api/posts/market_posts`, {
        params: {
          zipcode: zipcode,
        },
      });
      console.log(res);
      setItems(res.data.posts);
      setFilteredItems(res.data.posts);
    } catch (err) {
      console.log(err);
    }
    setSearchPerformed(true);
  };

  const handleFilter = (filterText) => {
    const regex = new RegExp(filterText, 'i');
    const newFilteredItems = items.filter((item) => regex.test(item.itemName));
    setFilteredItems(newFilteredItems);
  };

  return (
    <div className="min-h-screen">
      <Navbar />
      <div className='flex justify-center'>
      <SearchBar onSearch={handleSearch} />
      {searchPerformed && 
        <FilterBar onFilter={handleFilter} />
      }
      </div>
      <div className="grid grid-cols-3 gap-4 w-5/6 mx-auto">
        {filteredItems.map((item, index) => (
          <div key={index} className="p-4">
            <ItemCard itemName={item.itemName} />
          </div>
        ))}
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  );
};

export default Market;
