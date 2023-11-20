import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Modal from "../components/Modal"
import { useModal } from "../context/ModalContext";



const AddBudgetForm = ({ onBudgetAdded }) => {
  const navigate = useNavigate();
  const { isModalOpen, openModal, closeModal } = useModal();

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
        navigate("");


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
    <Modal isOpen={isModalOpen} onClose={closeModal}>
    <div className="mx-auto md:w-1/2  bg-white p-4 rounded-md">
      <p className="text-center font-bold text-2xl mb-4">Add a Budget</p>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <label htmlFor="budgetName" className="font-semibold text-gray-700">
          Budget Name:
          <input
            type="text"
            value={budgetName}
            onChange={(e) => setBudgetName(e.target.value)}
            required
            className="w-full p-2 border border-gray-300 focus:outline-none"
          />
        </label>
        <label htmlFor="budgetAmount" className="font-semibold text-gray-700">
          Budget Amount:
          <input
            type="number"
            value={budgetAmount}
            onChange={(e) => setBudgetAmount(e.target.value)}
            required
            className="w-full p-2 border border-gray-300 focus:outline-none"
          />
        </label>
        <div >
          {" "}
          <button type="submit" className="mt-4  bg-black p-2 text-white hover:bg-[#EE6338]">Add Budget</button>
        </div>{" "}
      </form>
    </div>
    </Modal>
  );
};

export default AddBudgetForm;
