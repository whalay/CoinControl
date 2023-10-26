import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Dashboard = () => {

  const { user} = useAuth();



  return (
    <div className="container mx-auto mt-8 p-4">
      <div className="md:flex justify-between items-center"><h1 className="text-3xl font-semibold mb-4">Welcome, {user.username}!</h1>
      <Link to="/logout">
         {" "}
         <button className="bg-gray-100 px-6 py-2">Logout</button>
       </Link></div>
      <section className="bg-white p-6 rounded-md shadow-md mb-4">
        <h2 className="text-xl font-semibold mb-4">Account Overview</h2>
        {/* Display account balance, transactions, etc. */}
        {/* Add appropriate components and styling here */}
      </section>

      <section className="bg-white p-6 rounded-md shadow-md mb-4">
        <h2 className="text-xl font-semibold mb-4">Income and Expenses</h2>
        {/* Display charts or tables showing income and expenses */}
        {/* Add appropriate components and styling here */}
      </section>

      <section className="bg-white p-6 rounded-md shadow-md mb-4">
        <h2 className="text-xl font-semibold mb-4">Budget Planning</h2>
        {/* Provide tools for budget planning */}
        {/* Add appropriate components and styling here */}
      </section>

      <section className="bg-white p-6 rounded-md shadow-md mb-4">
        <h2 className="text-xl font-semibold mb-4">Investments</h2>
        {/* Display information about investments */}
        {/* Add appropriate components and styling here */}
      </section>

      {/* Add more sections as needed for your finance dashboard */}
    </div>
  );
};


export default Dashboard;
