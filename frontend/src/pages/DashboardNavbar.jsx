import { useAuth } from "../context/AuthContext";
import { RxHamburgerMenu } from "react-icons/rx";

import coincontrol from "../assets/images/coincontrol.png";
import DashboardMobileNav from "../components/DashboardMobileNav";

const DashboardNavbar = () => {
  const { user } = useAuth();
  // const user = localStorage.getItem("userData");

  return (
    <div className="md:flex justify-between items-center mb-4">
      <div className="flex flex-row justify-between">
        <img src={coincontrol} alt="logo" className=" md:h-15 h-12" />
        <div className="md:hidden">
        <DashboardMobileNav />

        </div>
      </div>
      <div className="flex flex-row items-center justify-between md:gap-10">
        <h1 className="text-2xl  ">Welcome, <span className="text-[#EE6338] font-semibold">{user?.username}!</span></h1>
        <p>Monday, 27th June 2021</p>
      </div>
      <input
        type="search"
        className="border rounded-md focus:outline-none p-1"
      />
    </div>
  );
};

export default DashboardNavbar;
