import { useState } from "react";
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';

import signup from "../assets/images/signup-bg.png";
import coincontrol from "../assets/images/coincontrol.png";

const SignupPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirm_password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };
  const handleGoogleSignUp = () => {
    // Implement Google Sign-In logic
    console.log("Signing in with Google");
  };

  const handleSubmit = async(e) => {
    e.preventDefault();
   
    try {
      // Assuming you have a backend API endpoint for user registration
      const response = await axios.post('http://127.0.0.1:5000/api/v1/register', formData);
    
      console.log('Registration successful:', response.data);
      // Optionally, you can redirect or perform other actions upon successful registration
      navigate('/login');
    } catch (error) {
      if (error.response) {
        // The request was made, but the server responded with a status code
        // that falls out of the range of 2xx
        console.error('Registration failed:', error.response.data);
        console.error('Status code:', error.response.status);
      } else if (error.request) {
        // The request was made but no response was received
        console.error('No response received from the server');
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error('Error during registration:', error.message);
      }
    }
    console.log("Form submitted:", formData);
  };
  return (
    <div className="h-screen  md:flex items-center md:px-10 px-3 ">
      <div className="md:w-1/2">
      <Link to='/'>
        <img src={coincontrol} alt="logo" className=" h-16 " /></Link>
        <img src={signup} alt="" className=""/>
      </div>

      <div className="max-w-md md:max-w-xl mx-auto   mt-8 p-6 bg-gray-200 rounded-xl  space-y-5  shadow-md md:w-1/2">
        <h2 className="text-2xl font-semibold mb-4">Create an account</h2>
        <p className="mb-4">
          welcome to the future of secure finance management
        </p>
        <form onSubmit={handleSubmit}>
          <div className="mb-4 flex space-x-4">
            <div className="w-1/2">
              <label
                htmlFor="username"
                className="block text-gray-600 font-medium"
              >
                Username
              </label>
              <input
                type="text"
                id="username"
                name="username"
                value={formData.username}
                onChange={handleChange}
                className="form-input mt-1 block w-full focus:outline-none p-1 rounded-xl"
                required
              />
            </div>
            <div className="w-1/2">
              <label
                htmlFor="email"
                className="block text-gray-600 font-medium"
              >
                Email
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="form-input mt-1 block w-full focus:outline-none p-1 rounded-xl"
                required
              />
            </div>
          </div>
          <div className="mb-4">
            <label
              htmlFor="password"
              className="block text-gray-600 font-medium"
            >
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="form-input mt-1 block w-full focus:outline-none p-1 rounded-xl"
              required
            />
          </div>
          <div className="mb-4">
            <label
              htmlFor="confirm_password"
              className="block text-gray-600 font-medium"
            >
              Confirm Password
            </label>
            <input
              type="password"
              id="confirm_password"
              name="confirm_password"
              value={formData.confirm_password}
              onChange={handleChange}
              className="form-input mt-1 block w-full focus:outline-none p-1 rounded-xl"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 w-full"
          >
            Sign Up
          </button>
          <div className="mt-4">
            <button
              type="button"
              onClick={handleGoogleSignUp}
              className="w-full text-white p-2 rounded-md mt-2 hover:bg-red-600 focus:outline-none focus:ring focus:border-red-300"
            >
              Sign in with Google
            </button>
          </div>
     

        <p className="mt-4 text-center text-gray-600">
          Already have an account?{" "}
          <button
            type="button"
            className="text-blue-500 hover:underline focus:outline-none"
          >
           Log in
          </button>
        </p>
        </form>
      </div>
    </div>
  );
};

export default SignupPage;
