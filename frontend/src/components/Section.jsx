import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Section = () => {
  const { isLoggedIn } = useAuth();

  return (
    <div className="bg-[#DFE2E5] absolute left-0  w-full mb-60">
      <div className="m-10 p-5 bg-[#62618F] text-center space-y-3 rounded-xl text-white">
        <h1 className="text-2xl md:text-4xl font-semibold">
          Start managing your Finance today!
        </h1>
        <p className="text-lg md:text-xl">
          Sign up now and take control of your financial future.
        </p>
        <div className={`${isLoggedIn} ? "hidden" : "block"`}>
          <button className="px-10 py-2 bg-gray-400 rounded-xl text-white shadow-md hover:bg-[#EE6338] hover:border-none hover:text-white">
            <Link to="register">Sign Up</Link>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Section;
