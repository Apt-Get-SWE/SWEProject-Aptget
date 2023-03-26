import { createContext, useState, useEffect } from 'react'
import axios from 'axios'

const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
  const [loggedIn, setLoggedIn] = useState(false)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const checkLoginStatus = async () => {
      try {
        const res = await axios.get("/api/login/restricted_area")
        if (res.data && res.data.Status === "Success") {
          setLoggedIn(true)
        }
        setLoading(false)
      } catch (error) {
        console.error(error)
      }
    }

    checkLoginStatus()
  }, [])

  return (
    <AuthContext.Provider value={{ loggedIn, setLoggedIn, loading }}>
      {children}
    </AuthContext.Provider>
  )
}

export default AuthContext