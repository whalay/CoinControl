import { useState, useEffect } from "react";
import axios from "axios";

const DashBoardBudget = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const url = `${import.meta.env.VITE_APP_URL}/budgets`;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem("accessToken");
        const response = await axios.get(url, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.status === 200 || response.data.status === "success") {
          console.log(response.data.data)
          setData(response.data.data.data);
        } else {
          throw new Error("Failed to fetch budget");
        }
      } catch (error) {
        console.error("Error fetching user budget:", error);
        setError("Failed to fetch budget. Please try again.");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return (
    <section className="p-6 rounded-md shadow-md mb-4">
      <h2 className="text-2xl font-semibold mb-4">Budget</h2>
      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}
      <div className="flex flex-col md:flex-row justify-start gap-5">
        {Array.isArray(data) && data.length > 0 ? (
          data.map((budget) => (
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
  );
};

export default DashBoardBudget;
