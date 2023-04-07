import React from 'react'
import Footer from '../Components/Footer/Footer'
import Navbar from '../Components/NavBar/Navbar'
import ItemCard from '../Components/ItemCard/ItemCard'

const Market = () => {
  return (
    <div className="min-h-screen">
      <Navbar />
      <div className="grid grid-cols-3 gap-4 w-5/6 mx-auto">
        <div className='p-4'>
          <ItemCard itemName="TestItem" />
        </div>
        <div className='p-4'>
          <ItemCard itemName="TestItem" />
        </div>
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  )
}

export default Market