import axios from 'axios';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import ItemInfoForm from '../Forms/ItemInfoForm';

const MyItemCard = (props) => {
  const navigate  = useNavigate()
  function deletePost(pid)  {
    console.log(pid)
    axios.delete(`/api/posts/posts?pid=${pid}`)
    navigate(0)
  };
  const displayPrice = () => {
    return props.price ? `$${props.price}` : '$0.00';
  };
  const [isUpdateOpen, setIsUpdateOpen] = useState(false);
  const closeFormIfClickedOutside = (event) => {
    if (event.target === event.currentTarget) {
      setIsUpdateOpen(false);
    }
  };

  return (
    <div className="w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
      <div>
        {
          props.image ?
          <img className="object-cover w-full h-56 rounded-t-lg" src={props.image} alt="item" />
          :
          // placeholder image, when no image is provided
          <img className="object-cover w-full h-56 rounded-t-lg" src={`https://picsum.photos/200/300.jpg`} alt="item" />
        }
      </div>
      <div className="px-5 pb-5 pt-2">
        <div>
          <h5 className="text-3xl font-semibold tracking-tight text-gray-900 dark:text-white">{props.itemName}</h5>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-xl font-bold text-gray-900 dark:text-white">{displayPrice()}</span>
          <button onClick={() =>deletePost(props.pid)}  className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">{
            "delete"}</button>
          <button onClick={() => setIsUpdateOpen(true)} className="text-white bg-yellow-500 hover:bg-yellow-600 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-yellow-600 dark:hover:bg-yellow-700 dark:focus:ring-yellow-800">
              Update
            </button>
        </div>
        </div>
        {isUpdateOpen && (
        <div 
          className="fixed inset-0 z-10 bg-black bg-opacity-50 flex items-center justify-center"
          onClick={closeFormIfClickedOutside}
          >
          <div className="bg-white w-5/6 md:w-1/2 lg:w-1/3 p-6 rounded-lg">
            <button
              onClick={() => setIsUpdateOpen(false)}
              className="absolute right-4 top-4 text-gray-500 hover:text-gray-800"
            >
              &times;
            </button>
            <ItemInfoForm postData={props} /> 
          </div>
        </div>
      )}
        </div>
    );
};

export default MyItemCard;