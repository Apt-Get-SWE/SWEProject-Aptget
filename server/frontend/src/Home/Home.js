import './Home.css';
import spotlight from "./spotlight.svg"

function Home() {
  return (
    <div className="Home">

      <div className="Navbar">
        <script src="https://apis.google.com/js/platform.js" async defer></script>
        <a className="LoginLink" href="/login">
          <div className="Login">
             <span className="login-text">Login</span>
          </div>
        </a>
      </div>

      <div className="Body">

        <div>
          <span className="title-text green">AptGet.</span>
          <span className="title-text black">nyc</span>
        </div>

        <div className="BottomBox">

          <span className="Subtitle">find cheap stuff in your building.</span>

          <div className="SearchBar">
            <img src={spotlight} />
            <input className="AddressInput" type="text" name="address" placeholder="what's your address?" />
          </div>

        </div>

      </div>

    </div>
  );
}

export default Home;
