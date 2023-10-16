import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import RootLayout from '../../frontend/src/pages/RootLayout';
import Homepage from '../../frontend/src/pages/Homepage';
import LoginPage from '../../frontend/src/pages/LoginPage';
import SignupPage from '../../frontend/src/pages/SignupPage';

const router = createBrowserRouter([
  {
    path: '/',
  element: <RootLayout />,
  // errorElement: <ErrorPage />,
  children: [
    {
      index: true,
      element: <Homepage />
    },
  ]
    },
    {
      path: 'login',
      element: <LoginPage/>
    },
    {
      path: 'signup',
      element: <SignupPage/>
    },
]);

function App() {

  return <RouterProvider router={router} />;
}

export default App
