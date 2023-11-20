import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import jsCookie from 'js-cookie'


const PrivateRoutes = ({children}) => {
  const { isLoggedIn } = useAuth();
  const storedToken = jsCookie.get("accessToken");


  if (!storedToken){
    return <Navigate to="/login" />
  }

  return children
};
export default PrivateRoutes;
