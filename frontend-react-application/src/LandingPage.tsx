import "./LandingPage.css";
import { Link } from "react-router-dom";
import lpImage from "./assets/lp11.png"; // 

const LandingPage = () => {
  return (
    <div className="landing-page">
      <div className="left">
        <header className="logo">Logo</header>
        <div className="intro">
          <h1>Document<br />Management<br />System</h1>
          <hr />
          <div className="actions">
            <Link to="/add"><button>Add new docs</button></Link>
            <Link to="/view"><button>View existing docs</button></Link>
            <Link to="/edit"><button>Edit documents</button></Link>
            <Link to="/delete"><button>Delete documents</button></Link>
          </div>
        </div>
      </div>

      <div className="right">
        <nav>
          <a href="#">Home</a>
          <a href="#">Services</a>
          <a href="#">Contact</a>
          <a href="#">Sign in</a>
        </nav>
        <div className="image-wrapper">
          <img
            src={lpImage}
            alt="Document visual"
            className="landing-image"
          />
        </div>
      </div>
    </div>
  );
};
export default LandingPage;
