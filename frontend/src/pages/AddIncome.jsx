import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const AddIncome = () => {
  const [amount, setAmount] = useState("");
  const navigate = useNavigate()
 

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.put(
        `${import.meta.env.VITE_APP_URL}/income`,
        {
          amount: parseFloat(amount), // Assuming amount is a number
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.status === 201 || response.data.status === "success") {
        // Clear form fields
        setAmount("");
        navigate('/dashboard/me');

        // Notify parent component about the added budget
      } else {
        throw new Error("Failed to add income");
      }
    } catch (error) {
      console.error("Error adding income:", error);
    }
  };

  return (
    <div className="md:max-w-xl max-w-md bg-gray-300 p-5">
      <p className="text-center font-bold text-2xl">Add Income</p>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-5 py-5 text-xl">
        <label>
          Top Up Amount:
          <input
            type="text"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
            className="p-2 outline-none m-1"
          />
        </label>
       
        <div >
          {" "}
          <button type="submit" className="bg-black p-2 text-white hover:bg-[#EE6338]">Top Up</button>
        </div>{" "}
      </form>
    </div>
  );
};

export default AddIncome;
