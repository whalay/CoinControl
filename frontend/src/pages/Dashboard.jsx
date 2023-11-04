import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const Dashboard = () => {
  const [incomeData, setIncomeData] = useState();
  const [budgetData, setBudgetData] = useState([]);
  const [loading, setLoading] = useState(true);

  const incomeUrl = `${import.meta.env.VITE_APP_URL}/income`;
  const budgetsUrl = `${import.meta.env.VITE_APP_URL}/budgets`;

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    axios
      .get(incomeUrl, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        // withCredentials: true,
      })
      .then((incomeResponse) => {
        if (incomeResponse.status === 200) {
          setIncomeData(incomeResponse.data.data.income)
          setLoading(false);

        } else if (incomeResponse.status === 404) {
          console.log(false);
        } else {
          throw new Error("Failed to fetch user store");
        }
      })
      .catch((error) => {
        console.error("Error fetching user store:", error);
      });

      axios
      .get(budgetsUrl, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        // withCredentials: true,
      })
      .then((budgetResponse) => {
        if (budgetResponse.status === 200) {
          setBudgetData(budgetResponse.data.data.data)
          setLoading(false);

        } else if (budgetResponse.status === 404) {
          console.log(false);
        } else {
          throw new Error("Failed to fetch user store");
        }
      })
      .catch((error) => {
        console.error("Error fetching user store:", error);
      })

  }, []);

  return (
    <div className="container mx-auto block md:flex flex-row  p-4 justify-between gap-10">
      <div className="flex-1">
        {" "}
        <section className="bg-white  p-6 rounded-md shadow-md mb-4 flex flex-col md:flex-row justify-between">
          <div>
            <h2 className="text-xl font-semibold mb-2 text-[#EE6338]">
              Total Balance
            </h2>
            <p className="text-xl font-bold">${incomeData}</p>
          </div>
          <div>
            <h2 className="text-xl font-semibold my-4 md:my-0 text-[#EE6338]">
              Quick Actions
            </h2>
            <span className="flex flex-row gap-5">
              {" "}
              <Link to="comingsoon">
                {" "}
                <h6 className="hover:text-[#EE6338]">Top up</h6>
              </Link>
              <Link to="comingsoon">
                {" "}
                <h6 className="hover:text-[#EE6338]">Transfer</h6>
              </Link>
              <Link to="comingsoon">
                {" "}
                <h6 className="hover:text-[#EE6338]">Withdraw</h6>
              </Link>
            </span>
          </div>
          {/* Add appropriate components and styling here */}
        </section>
        <section className="p-6 rounded-md shadow-md mb-4">
      <h2 className="text-2xl font-semibold mb-4">Budget</h2>
      {loading && <p>Loading...</p>}
      {/* {error && <p className="text-red-500">{error}</p>} */}
      <div className="flex flex-col md:flex-row justify-start gap-5">
        {Array.isArray(budgetData) && budgetData.length > 0 ? (
          budgetData.map((budget) => (
            <div className="rounded-md shadow-md p-2" key={budget.id}>
              <h6 className="text-xl font-semibold mb-1">{budget.name}</h6>
              <p className="font-semibold text-md">${budget.amount}</p>
              <p>{budget.date_created}</p>
            </div>
          ))
        ) : (
          <p>No budget data available.</p>
        )}
      </div>
    </section>
        <section className="p-6 rounded-md shadow-md mb-4">
          <h2 className="text-2xl font-semibold mb-4 text-[#EE6338]">
            Money Statistics
          </h2>
          <div className="flex flex-col md:flex-row justify-start gap-5">
            <div className="rounded-md shadow-md p-2">
              <h6 className="text-xl font-semibold mb-1">Total Income</h6>
              <p className="font-semibold text-md">$3,000,000</p>
            </div>

            <div className="rounded-md shadow-md p-2">
              <h6 className="text-xl font-semibold mb-1">Total Expenses</h6>
              <p className="font-semibold text-md">$3,000,000</p>
            </div>
          </div>
        </section>
      </div>
      <div className="flex-1/2 border p-5">
        <h1 className="text-xl pb-1 text-[#EE6338]">Transactions</h1>
        <h5>Recent expenses</h5>
        <div className="flex flex-row justify-between gap-10 border p-3">
          <h3>Airforce-1</h3>
          <p>$35,000</p>
        </div>
        <p className="text-center">show more ...</p>
      </div>
    </div>
  );
};

export default Dashboard;
