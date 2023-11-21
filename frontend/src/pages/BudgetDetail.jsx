// BudgetDetail.js
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import jsCookie from 'js-cookie'

import axios from "axios";

const BudgetDetail = () => {
  const { budgetId } = useParams();
  const [budget, setBudget] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBudgetDetail = async () => {
      try {
        const token = jsCookie.get("accessToken");
        const response = await axios.get(
          `${import.meta.env.VITE_APP_URL}/budgets/${budgetId}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (response.status === 200) {
          setBudget(response.data.data);
        } else {
          throw new Error("Failed to fetch budget detail");
        }
      } catch (error) {
        console.error("Error fetching budget detail:", error);
        setError("Failed to fetch budget detail. Please try again.");
      } finally {
        setLoading(false);
      }
    };

    fetchBudgetDetail();
  }, [budgetId]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  if (!budget) {
    return <p>No data available for this budget.</p>;
  }

  return (
    <div className="text-2xl">
      <h2 className="text-2xl">{budget.name}</h2>
      <p>Amount: ${budget.amount}</p>
      <p>Date Created: {budget.date_created}</p>
      {/* Add more details as needed */}
    </div>
  );
};

export default BudgetDetail;
