import { useState } from "react";
import { Link, Navigate } from "react-router-dom";
import axios from "axios";


import { useAuth } from "../context/AuthContext";
import { AiOutlineMail } from "react-icons/ai";
import { AiOutlineLock } from "react-icons/ai";

import signin from "../assets/images/signin-bg.png";
import coincontrol from "../assets/images/coincontrol.png";

const LoginPage = () => {

  const { login, isLoggedIn} = useAuth();
  const [errors, setErrors] = useState({}); // New state for errors

  const [formState, setFormState] = useState({
    email: "",
    password: "",
    rememberMe: false, // New state for "Remember Me"
  });
  const url = `${import.meta.env.VITE_APP_URL}/login`;
  const handleLogin = async () => {
    const userData = {
      email: formState.email,
      password: formState.password,
      rememberMe: formState.rememberMe, // Include "Remember Me" value
    };
    // Call the login function with userData
    try {
      // Assuming you have a backend API endpoint for user authentication
      const response = await axios.post(
        url,
        userData
      );

      // If authentication is successful, set the user data in the state
      // setUser(response.data.data);
      // setIsLoggedIn(true);
      // console.log(response.data.data);

      // You can save it in local storage or a cookie
      // localStorage.setItem("accessToken", response.data.data.access_token);
      // localStorage.setItem('userData', JSON.stringify(response.data.data));
      login(response);
    } catch (error) {
      // Handle login failure
        setErrors(error.response.data);

      // Optionally, you can throw an error or show an error message
      // throw new Error("Login failed");
    }
  };

  const handleGoogleSignIn = () => {
    // Implement Google Sign-In logic
    console.log("Signing in with Google");
  };

  const handleSignup = () => {
    // Implement your signup logic here
    console.log("Redirecting to signup page");
  };

  return isLoggedIn ? (
    <Navigate to="/dashboard" />
  ) : (
    <div className="h-screen flex md:flex-row flex-col items-center md:px-10 px-3">
      <div className="md:w-1/2">
        <Link to="/">
          <img src={coincontrol} alt="logo" className=" h-16 " />
        </Link>

        <img src={signin} alt="" />
      </div>
      <div className="max-w-md mx-auto md:w-1/2 mt-8 shadow-md bg-gray-200 rounded-xl md:p-10 p-3 space-y-5">
        <h2 className="text-3xl font-semibold ">Welcome Back!</h2>
        <p>Start managing your finance faster and better.</p>

        <form>
          <div className="mb-4 relative">
            <label htmlFor="email" className="sr-only">
              Email
            </label>
            <div className="relative w-full">
              <AiOutlineMail className="absolute left-3 top-1/2 transform -translate-y-1/2 w-6 h-6 text-gray-500" />
              <input
                type="email"
                id="email"
                placeholder="Enter your email"
                className="w-full p-2 pl-10 bg-[#F2F2F2] border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                onChange={(e) =>
                  setFormState({ ...formState, email: e.target.value })
                }
                value={formState.email}
              />
            </div>
          </div>

          <div className="mb-4 relative">
            <label htmlFor="password" className="sr-only">
              Password
            </label>
            <div className="relative w-full">
              <AiOutlineLock className="absolute left-3 top-1/2 transform -translate-y-1/2 w-6 h-6 text-gray-500" />
              <input
                type="password"
                id="password"
                placeholder="Enter your password"
                className="w-full p-2 pl-10 bg-[#F2F2F2] border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                value={formState.password}
                onChange={(e) =>
                  setFormState({ ...formState, password: e.target.value })
                }
              />
            </div>
          </div>

          <div className="mb-4 flex items-center">
            <input
              type="checkbox"
              id="rememberMe"
              className="mr-2"
              checked={formState.rememberMe}
              onChange={(e) =>
                setFormState({ ...formState, rememberMe: e.target.checked })
              }
            />
            <label htmlFor="rememberMe" className="text-sm text-gray-600">
              Remember me
            </label>
          </div>
          {errors && (
            <div className="text-red-500 text-sm mt-2">{errors.message}</div>
          )}
          <button
            type="button"
            onClick={handleLogin}
            className="w-full hover:bg-[#EE6338] text-black p-2 rounded-md  focus:outline-none focus:ring focus:border-blue-300"
          >
            Login
          </button>

          <div className="mt-4">
            {/* Placeholder image and text */}
            <p className="text-center text-gray-600">Or</p>
            <button
              type="button"
              onClick={handleGoogleSignIn}
              className="w-full bg-[#F2F2F2] text-black p-2 rounded-md mt-2 hover:bg-[#EE6338] focus:outline-none focus:ring focus:border-red-300"
            >
              Sign in with Google
            </button>
          </div>
        </form>

        <p className="mt-4 text-center text-gray-600">
          Don't have an account?{" "}
          <Link to="/register">
            {" "}
            <button
              type="button"
              onClick={handleSignup}
              className="text-blue-500 hover:underline focus:outline-none hover:text-[#EE6338]"
            >
              Sign up
            </button>
          </Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
