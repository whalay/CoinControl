import  { useState } from "react";
import { AiOutlineMail } from "react-icons/ai";
import { AiOutlineLock} from "react-icons/ai";

import signin from "../assets/images/signin-bg.png";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);

  const handleLogin = () => {
    // Implement your login logic here
    console.log(
      "Logging in with:",
      email,
      password,
      "Remember Me:",
      rememberMe
    );
  };

  const handleGoogleSignIn = () => {
    // Implement Google Sign-In logic
    console.log("Signing in with Google");
  };

  const handleSignup = () => {
    // Implement your signup logic here
    console.log("Redirecting to signup page");
  };
  return (
    <div className="h-screen flex md:flex-row flex-col items-center px-10">
      <div className="md:w-1/2">
        <img src={signin} alt="" />
      </div>
      <div className="max-w-md mx-auto md:w-1/2 mt-8 shadow-md bg-gray-200 rounded-xl p-10 space-y-5">
        <h2 className="text-3xl font-semibold ">Welcome Back!</h2>
        <p>Start managing your finance faster and better.</p>

        <form>
          <div className="mb-4 relative">
            <label
              htmlFor="email"
              className="block text-gray-600 text-sm font-medium mb-2"
            >
              Email
            </label>
            <input
              type="email"
              id="email"
              placeholder=""
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
              onChange={(e) => setEmail(e.target.value)}
            />
            <AiOutlineMail className="absolute left-3 top-1/2 transform  w-6 h-6" />
            <span className="absolute left-10 top-1/2 transform  text-gray-500">
              you@coincontrol.com
            </span>
          </div>

          <div className="mb-4 relative">
            <label
              htmlFor="password"
              className="block text-gray-600 text-sm font-medium mb-2"
            >
              Password
            </label>
            <input
              type="password"
              id="password"
              placeholder=""
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
              onChange={(e) => setPassword(e.target.value)}
            />
            <AiOutlineLock className="absolute left-3 top-1/2 transform  w-6 h-6" />
            <span className="absolute left-10 top-1/2 transform  text-gray-500">
              Atleast 6 characters
            </span>
          </div>

          <div className="mb-4 flex items-center">
            <input
              type="checkbox"
              id="rememberMe"
              className="mr-2"
              checked={rememberMe}
              onChange={() => setRememberMe(!rememberMe)}
            />
            <label htmlFor="rememberMe" className="text-sm text-gray-600">
              Remember me
            </label>
          </div>

          <button
            type="button"
            onClick={handleLogin}
            className="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300"
          >
            Login
          </button>

          <div className="mt-4">
            {/* Placeholder image and text */}
            <p className="text-center text-gray-600">Or sign in with</p>
            <button
              type="button"
              onClick={handleGoogleSignIn}
              className="w-full bg-red-500 text-white p-2 rounded-md mt-2 hover:bg-red-600 focus:outline-none focus:ring focus:border-red-300"
            >
              Sign in with Google
            </button>
          </div>
        </form>

        <p className="mt-4 text-center text-gray-600">
          Don't have an account?{" "}
          <button
            type="button"
            onClick={handleSignup}
            className="text-blue-500 hover:underline focus:outline-none"
          >
            Sign up
          </button>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
