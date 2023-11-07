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
import Budget from "./pages/Budget";
import AddIncome from "./pages/AddIncome";
import BudgetDetail from "./pages/BudgetDetail";

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
    path: "register",
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
            element: <Budget />,
          },
          {
            path: "budget/:budgetId",
            element: <BudgetDetail />,
          },
          {
            path: "income",
            element: <AddIncome />,
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
