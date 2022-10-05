import './Home.css';
import spotlight from "./spotlight.svg"

function Home() {
  return (
    <div className="Home">

      <div className="Navbar">
        <div className="Login">
        <p className="login-text">Log In</p>
        </div>
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
