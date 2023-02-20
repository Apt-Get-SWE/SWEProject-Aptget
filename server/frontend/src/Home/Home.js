import './Home.css';
import spotlight from "./spotlight.svg"
import axios from 'axios'
import { useState } from 'react';

function Home() {
  const [loggedIn, setLoggedIn] = useState(false)

  if (sessionStorage.getItem("loggedIn") !== "1" || loggedIn === false) {
    axios.get("/api/login/restricted_area").then((res) => {
      console.log(res.data.Status)
      if (res.data && res.data.Status === "Success") {
        sessionStorage.setItem("loggedIn", "1")
        setLoggedIn(true)
      }
    });
  }

  return (
    <div className="Home">

      <div className="Navbar">
        <script src="https://apis.google.com/js/platform.js" async defer></script>
        {
          loggedIn
            ? 
            <div></div>
            :
            <a className="LoginLink" href="/api/login/login">
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
