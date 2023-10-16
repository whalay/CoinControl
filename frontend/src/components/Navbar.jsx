import { Link } from "react-router-dom";
import coincontrol from "../assets/images/coincontrol.png";
import MobileNav from "./MobileNav";

const Navbar = () => {
  return (
    <div className="flex justify-between items-center ">
      <div className="">
        <img src={coincontrol} alt="logo" className=" h-20 " />
      </div>
      <div className="lg:hidden">
        <MobileNav className="" />
      </div>
      <div className="hidden md:flex justify-between items-center text-xl gap-10">
        <ul className="flex justify-between  items-center gap-10">
          <li>How it works</li>
          <li>About Us</li>
          <li>FAQ</li>
        </ul>
        <div className="hidden lg:flex justify-between items-center gap-10">
          <Link to="login">
            {" "}
            <button className="bg-gray-100 px-6 py-2">Login</button>
          </Link>
          <Link to="signup">
            <button className="border px-6 py-2">Create free account</button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
