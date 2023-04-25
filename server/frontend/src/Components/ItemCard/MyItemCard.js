import axios from 'axios';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const MyItemCard = (props) => {
  const navigate  = useNavigate()
  function deletePost(pid)  {
    console.log(pid)
    axios.delete(`/api/posts/posts?pid=${pid}`)
    navigate(0)
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
          <span className="text-xl font-bold text-gray-900 dark:text-white">{() => { return props.price ? `$${props.price}` : '$0.00'}}</span>
          <button onClick={() =>deletePost(props.pid)}  className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">{
            "delete"}</button>
        </div>
        </div>
        </div>
    );
};

export default MyItemCard;