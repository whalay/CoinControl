import { createContext, useContext, useState, useEffect,  } from "react";
// import axios from "axios";

// Create the AuthContext
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState();
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  // const [errors, setErrors] = useState({}); // New state for errors

  
    // Check for stored token during component initialization
    useEffect(() => {
      const storedUser = localStorage.getItem('userData');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
      setIsLoggedIn(true);
      
    }
    }, []);

  const login = async (response) => {

    // try {
      // Assuming you have a backend API endpoint for user authentication
      // const response = await axios.post(
      //   "http://127.0.0.1:5000/api/v1/login",
      //   userData
      // );

      // If authentication is successful, set the user data in the state
      setUser(response.data.data);
      setIsLoggedIn(true);
      // console.log(response.data.data);

    
      // You can save it in local storage or a cookie
      localStorage.setItem("accessToken", response.data.data.access_token);
      localStorage.setItem('userData', JSON.stringify(response.data.data));

      // console.log(response.data.data.access_token);
      // navigate('/dashboard');
      // window.location.href = "/dashboard";
    // } catch (error) {
    //   // Handle login failure
    //   console.error("Login failed:", error);
    //   console.error("Login failed:", error.response);
    //   console.error("Login failed:", error);

    //   setErrors(error);

    //   // Optionally, you can throw an error or show an error message
    //   throw new Error("Login failed");
    // }
  };

  const logout = () => {
    // Clear user data from the state

    setUser(null);
    setIsLoggedIn(false);

    // Optionally, clear any saved tokens or session data
    localStorage.removeItem("accessToken");
    localStorage.removeItem("userData");
  };

  // Provide the context values to the children
  const contextValues = {
    user,
    login,
    logout,
    isLoggedIn,
    // errors
  };

  return (
    <AuthContext.Provider value={contextValues}>
      {children}
    </AuthContext.Provider>
  );
};

// Create a custom hook to access the AuthContext values
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
