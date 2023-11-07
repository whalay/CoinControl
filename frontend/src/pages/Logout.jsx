import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import axios from "axios";

const Logout = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  useEffect(() => {
    const url = `${import.meta.env.VITE_APP_URL}/logout`;
    axios.post(url);
    // Perform logout when the component mounts
    logout();
    navigate("/login");
  }, []); // The dependency array ensures that useEffect runs only once when the component mounts

  return <div>Logging out ...</div>;
};

export default Logout;
