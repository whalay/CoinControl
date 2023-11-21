import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import axios from "axios";
import jsCookie from 'js-cookie'


const Logout = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  useEffect(() => {
    const token =jsCookie.get("accessToken");

    const url = `${import.meta.env.VITE_APP_URL}/logout`;
    axios.post(url, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    // Perform logout when the component mounts
    logout();
    navigate("/login");
  }, []); // The dependency array ensures that useEffect runs only once when the component mounts

  return <div>Logging out ...</div>;
};

export default Logout;
