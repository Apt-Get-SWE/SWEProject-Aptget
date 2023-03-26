import './Home.css';
import spotlight from "./spotlight.svg"
import axios from 'axios'
import { useContext } from 'react';
import AuthContext from '../Auth/AuthProvider';

function Home() {
  const { loggedIn, setLoggedIn } = useContext(AuthContext)

  const handleLogin = async () => {
      window.location.href = "/api/login/login"
  }

  const handleAuth = async () => {
    if (!loggedIn) {
      axios.get("/api/login/restricted_area").then((res) => {
        if (res.data && res.data.Status === "Success") {
          setLoggedIn(true)
        }
      });
    }
  }


  return (
    <div className="Home" onLoad={handleAuth}>

      <div className="Navbar">
        <script src="https://apis.google.com/js/platform.js" async defer></script>
        {
          loggedIn
            ? 
            <div className='LoggedIn'>
              <span className="login-text">Dashboard</span>
            </div>
            :
            <a className="LoginLink" onClick={handleLogin}>
              <div className="Login">
                <span className="login-text">Login</span>
              </div>
            </a>
        }
      </div>

      <div className="Body">

        <div>
          <span className="title-text green">AptGet.</span>
          <span className="title-text black">nyc</span>
        </div>

        <div className="BottomBox">

          <span className="Subtitle">find cheap stuff in your building.</span>

          <div className="SearchBar">
            <img src={spotlight} alt="spotlight" />
            <input className="AddressInput" type="text" name="address" placeholder="what's your address?" />
          </div>

        </div>

      </div>

    </div>
  );
}

export default Home;
