import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
const RootLayout = () => {
  return (
    <div className="md:px-20 px-5">
      <Navbar />

      <main className="">
        {/* {navigation.state === 'loading' && <p>Loading...</p>} */}
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default RootLayout;
