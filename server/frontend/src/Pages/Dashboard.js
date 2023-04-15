import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import ItemInfoForm from '../Components/Forms/ItemInfoForm'; // Make sure to import ItemCard
import ItemCard from '../Components/ItemCard/ItemCard'
import axios from 'axios';

const Dashboard = () => {
  const [showModal, setShowModal] = useState(false);
  const navigate = useNavigate();
  const [posts, setPosts] = useState([]);

  const geUserPosts = async () => {
    const post_res = await axios.get('/api/posts/posts?user=True');

    let data = [];
    for (const [_, value] of Object.entries(post_res.data.Data)) {
      const user_res = await axios.get(`/api/users/users?uid=${value.uid}`);

      let user = user_res.data.Data[value.uid]
      value.email = user.email
      value.phone = user.phone

      console.log(value)
      data.push(value);
    }

    return data;
  };

  useEffect(() => {
    const fetchPosts = async () => {
      const newPosts = await geUserPosts();
      setPosts(newPosts);
    };
    fetchPosts();
  }, []);
  
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
      <div className="w-5/6 mx-auto mt-7">
        <h1 className="text-5xl font-bold mb-2">Your Posts</h1>
        <div className="grid grid-cols-3 gap-4 w-5/6 mt-5">
          {
            posts.map((item, index) => (
              <div>
                <ItemCard key={index} email={item.email} phone={item.phone} itemName={item.title} price={item.price} />
              </div>
            ))
          }
        </div>
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  );
};

export default Dashboard;