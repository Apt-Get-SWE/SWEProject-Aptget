import React from 'react'
import Footer from '../Components/Footer/Footer'
import Navbar from '../Components/NavBar/Navbar'
import ItemCard from '../Components/ItemCard/ItemCard'

const Dashboard = () => {
  /**
   * TODO
   * Get list of posts and contact info (via 'users' endpoint) for each post
   * Map post data to ItemCard component
   */

  return (
    <div className="min-h-screen">
      <Navbar />
      <div className="flex flex-col justify-center items-center">
        <ItemCard itemName="TestItem"/>
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  )
}

export default Dashboard