import React, { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { RxHamburgerMenu } from "react-icons/rx";
import { FaTimes } from "react-icons/fa";

const DashboardMobileNav = () => {
  const { isLoggedIn } = useAuth();

  const [isOpen, setIsOpen] = useState(false);

  const hamburgerHandler = () => {
    setIsOpen((isOpen) => !isOpen);
  };

  const closeNav = () => {
    setIsOpen(false);
  };

  return (
    <div className="">
      <RxHamburgerMenu onClick={hamburgerHandler} className="z-20" />
      {isOpen && (
        <div
          className={`${
            isOpen
              ? "fixed top-0 left-0 bg-gray-100 w-1/2 h-screen text-black z-20"
              : "p-5"
          }`}
        >
          <FaTimes onClick={closeNav} className="absolute top-10 right-10" />
          <div
            className={`${
              isOpen ? "  absolute top-10 left-10 text-2xl" : "lg:hidden  "
            }`}
          >
            <ul className="text-2xl  space-y-10 py-10">
              <li onClick={closeNav}>
              <NavLink to="">Home</NavLink>
              </li>
              <li onClick={closeNav}>
                <Link to="budget">Budgets</Link>
              </li>
              <li onClick={closeNav}>
              <NavLink to="comingsoon">Analytics</NavLink>
              </li>
            </ul>
            <Link to="logout">
              <button className=" w-full bg-[rgb(238,99,56)]  py-2 px-4 hover:bg-[#EE6338] hover:text-white border ">
                Logout
              </button>
            </Link>
            {/* {isLoggedIn ? (
              <div className="lg:hidden flex flex-col space-y-10">
                {" "}
                <Link to="logout">
                  {" "}
                  <button className=
                  
                  " w-full bg-[#EE6338]  py-2 px-4 hover:bg-[#EE6338] hover:text-white border ">
                    Logout
                  </button>
                </Link>
                <Link to="dashboard">
                  {" "}
                  <button className="bg-gray-100  py-2 hover:bg-[#EE6338] hover:text-white">
                    Dashboard
                  </button>
                </Link>
              </div>
            ) : (
              <div className="lg:hidden flex flex-col space-y-10 ">
                <Link to="login">
                  {" "}
                  <button className=" w-full bg-[#EE6338]  py-2 px-4 hover:bg-[#EE6338] hover:text-white border ">
                    Login
                  </button>
                </Link>
                <Link to="register">
                  <button className="border px-4 py-2 hover:bg-[#EE6338] border-[#EE6338] hover:border-none hover:text-white">
                    Create free account
                  </button>
                </Link>
              </div>
            )} */}
          </div>
        </div>
      )}
    </div>
  );
};

export default DashboardMobileNav;
