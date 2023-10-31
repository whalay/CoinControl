import { RouterProvider, createBrowserRouter } from "react-router-dom";
import RootLayout from "../../frontend/src/pages/RootLayout";
import Homepage from "../../frontend/src/pages/Homepage";
import LoginPage from "../../frontend/src/pages/LoginPage";
import SignupPage from "../../frontend/src/pages/SignupPage";
import Dashboard from "./pages/Dashboard";
import DashboardLayout from "./pages/DashboardLayout";
import Logout from "./pages/Logout";
import PrivateRoutes from "./pages/PrivateRoutes";
import DashBoardBudget from "./pages/DashBoardBudget";
import ComingSoon from "./pages/ComingSoon";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    // errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        element: <Homepage />,
      },
    ],
  },
  {
    path: "login",
    element: <LoginPage />,
  },
  {
    path: "logout",
    element: <Logout />,
  },
  {
    path: "signup",
    element: <SignupPage />,
  },
  {
    path: "/dashboard",
    element: <PrivateRoutes />,
    // errorElement: <ErrorPage />,
    children: [
      {
        path: 'me',
        element: <DashboardLayout />,
        children: [
          {
            
            path: '',
            element: <Dashboard />,
          },
          {
            path: "budget",
            element: <DashBoardBudget />,
          },
          {
            path: "comingsoon",
            element: <ComingSoon />,
          },
        ]
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
