import DashboardNavbar from "./DashboardNavbar";
import { Outlet, Link, NavLink } from "react-router-dom";

const DashboardLayout = () => {
  return (
    <div className="p-10 relative container pb-10">
      <DashboardNavbar />

      <div className="absolute left-10 hidden md:block   ">
        <div className="flex flex-col justify-start h-screen ">
          <div className="border p-5">
            {/* <h1 className="text-start  py-5">Menu</h1> */}
            <ul className="flex flex-col items-start gap-10">
            <li className="hover:text-[#EE6338]">
                <NavLink to="">Dashboard</NavLink>
              </li>
              <li className="hover:text-[#EE6338]">
                <NavLink to="budget">Budgets</NavLink>
              </li>
              <li className="hover:text-[#EE6338]">
                <NavLink to="comingsoon">Analytics</NavLink>
              </li>
            </ul>
          </div>
          <div className="border p-5">
            <h1 className="text-start pb-10 py-5">General</h1>
            <ul className="flex flex-col items-start gap-10 ">
              <li className="hover:text-[#EE6338]">
              <Link to="comingsoon">Settings</Link>
              </li>
              <li className="hover:text-[#EE6338]">
                <Link to="comingsoon">Help/Support</Link>
              </li>
            </ul>
          </div>
          <div className="p-5">
            <Link to="/logout">
              <h1 className="hover:text-[#EE6338]">Log out</h1>
            </Link>
          </div>
        </div>
      </div>
      <div className="md:pl-40  ">
        {" "}
        <Outlet />
      </div>
    </div>
  );
};

export default DashboardLayout;
