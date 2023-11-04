import React, { useState } from "react";
import axios from "axios";

const AddBudgetForm = ({ onBudgetAdded }) => {
  const [budgetName, setBudgetName] = useState("");
  const [budgetAmount, setBudgetAmount] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.post(
        `${import.meta.env.VITE_APP_URL}/budgets`,
        {
          name: budgetName,
          amount: parseInt(budgetAmount), // Assuming amount is a number
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.status === 201 || response.data.status === "success") {
        // Clear form fields
        setBudgetName("");
        setBudgetAmount("");

        // Notify parent component about the added budget
        onBudgetAdded(response.data.data);
      } else {
        throw new Error("Failed to add budget");
      }
    } catch (error) {
      console.error("Error adding budget:", error);
    }
  };

  return (
    <div className="md:max-w-xl max-w-md bg-gray-300 p-5">
      <p className="text-center font-bold text-2xl">Add a Budget</p>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-5 py-5 text-xl">
        <label>
          Budget Name:
          <input
            type="text"
            value={budgetName}
            onChange={(e) => setBudgetName(e.target.value)}
            required
            className="p-2 outline-none m-1"
          />
        </label>
        <label>
          Budget Amount:
          <input
            type="number"
            value={budgetAmount}
            onChange={(e) => setBudgetAmount(e.target.value)}
            required
            className="p-2 outline-none m-1"
          />
        </label>
        <div >
          {" "}
          <button type="submit" className="bg-black p-2 text-white hover:bg-[#EE6338]">Add Budget</button>
        </div>{" "}
      </form>
    </div>
  );
};

export default AddBudgetForm;
