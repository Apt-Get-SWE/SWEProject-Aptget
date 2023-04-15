import React from 'react'
import Footer from '../Components/Footer/Footer'
import Navbar from '../Components/NavBar/Navbar'
import UserProfileForm from '../Components/Forms/UserProfileForm'

const Profile = () => {
  return (
    <div className="min-h-screen">
      <Navbar />
      <div className="w-5/6 mx-auto">
        <UserProfileForm />
      </div>
      <div className="sticky top-[100vh]">
        <Footer />
      </div>
    </div>
  )
}

export default Profile