import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Footer from '../Components/Footer/Footer';
import Navbar from '../Components/NavBar/Navbar';
import MyItemCard from '../Components/ItemCard/MyItemCard'
import Notification from '../Components/Notification/Notification';
import axios from 'axios';

const Dashboard = () => {
  const navigate = useNavigate();
  const [posts, setPosts] = useState([]);
  const [trigger, setTrigger] = useState(false);

  const geUserPosts = async () => {
    const post_res = await axios.get('/api/posts/posts?loadUser=True');

    let data = [];
    for (let [_, value] of Object.entries(post_res.data.Data)) {
      // if value.image starts with "data:image/png;base64," then it is already a base64 string
      // otherwise, it is a BSON object and we need to convert it to a base64 string
      if (value.image && !value.image.startsWith("data:image/png;base64,")) {
        value.image = "data:image/png;base64," + value.image.$binary.base64;
      }

      const user_res = await axios.get(`/api/users/users?uid=${value.uid}`);
      let user = user_res.data.Data
      value.email = user.email
      value.phone = user.phone

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
      <Notification trigger={trigger} title="You're all set" description="Successfully Updated Item Listing" actionPrompt="View Updated" action={
        () => navigate("/")
        // TODO: axios post item
      } />
      {
        trigger ?
          <div className="fixed top-0 left-0 w-full h-full bg-black opacity-50 z-10 pointer-events-auto"></div>
          :
          null
      }
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
                <MyItemCard key={index} image={item.image} email={item.email} phone={item.phone} itemName={item.title} price={item.price} pid={item.pid} setTrigger={setTrigger} />
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