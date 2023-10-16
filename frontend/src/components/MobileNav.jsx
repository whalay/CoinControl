import React, { useState } from "react";
import { RxHamburgerMenu } from "react-icons/rx";
import {FaTimes} from "react-icons/fa"

const MobileNav = () => {
  const [isOpen, setIsOpen] = useState(false);

  const hamburgerHandler = () => {
    setIsOpen((isOpen) => !isOpen);
  };

  const closeNav = () => {
    setIsOpen(false);
  };

  return (
    <div className="">
      <RxHamburgerMenu onClick={hamburgerHandler} className="z-50" />
      {isOpen && (
        <div
          className={`${
            isOpen ? "fixed top-0 left-0 bg-gray-100 w-full h-screen text-black z-20" : "p-5"
          }`}
        >
          <FaTimes onClick={closeNav} className="absolute top-10 right-10"/>
          <ul
            className={`${
              isOpen
                ? "  absolute top-10 left-10 flex flex-col   "
                : "lg:flex flex-col  hidden"
            } gap-5 text-xl font-bold`}
          >
            <li>How it works</li>
            <li>About Us</li>
            <li>FAQ</li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default MobileNav;
