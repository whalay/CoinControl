import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import coincontrol from "../assets/images/coincontrol.png";
import MobileNav from "./MobileNav";

const links = [
  { name: "How it works", url: "" },
  { name: "About Us", url: "" },
  { name: "FAQ", url: "" },
];

const Navbar = () => {
  const { isLoggedIn } = useAuth();
  return (
    <div className="flex justify-between items-center mt-4">
      <div className="">
        <img src={coincontrol} alt="logo" className=" md:h-15 h-20 " />
      </div>
      <div className="md:hidden">
        <MobileNav className="" />
      </div>
      <div className="hidden md:flex justify-between items-center text-xl gap-10">
        <ul className="flex justify-between  items-center gap-5">
          {links.map((link, index) => {
            return (
              <Link key={index}>
                <li className="hover:bg-[#EE6338] hover:text-white p-1">
                  {link.name}
                </li>
              </Link>
            );
          })}
        </ul>
        {isLoggedIn ? (
          <div>
            {" "}
            <Link to="logout">
              {" "}
              <button className="bg-gray-100 px-6 py-2">Logout</button>
            </Link>
            <Link to="dashboard">
              {" "}
              <button className="bg-gray-100 px-6 py-2 hover:bg-[#EE6338] hover:text-white">Dashboard</button>
            </Link>
          </div>
        ) : (
          <div className="hidden lg:flex justify-between items-center gap-10">
            <Link to="login">
              {" "}
              <button className="bg-gray-100 px-6 py-2 hover:bg-[#EE6338] hover:text-white">
                Login
              </button>
            </Link>
            <Link to="register">
              <button className="border px-6 py-2 hover:bg-[#EE6338] hover:border-none hover:text-white">
                Create free account
              </button>
            </Link>
          </div>
        )}
      </div>
    </div>
  );
};

export default Navbar;
