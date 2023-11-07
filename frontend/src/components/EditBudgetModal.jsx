// EditBudgetModal.js
import React, { useState, useEffect } from "react";

const EditBudgetModal = ({ isOpen, budget, onSave, onClose }) => {
  const [editedBudget, setEditedBudget] = useState({ ...budget });

  useEffect(() => {
    setEditedBudget({ ...budget });
  }, [isOpen, budget]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditedBudget((prevBudget) => ({
      ...prevBudget,
      [name]: value,
    }));
  };

  const handleSave = () => {
    onSave(editedBudget);
    onClose();
  };

  return (
    <div
      className={`${
        isOpen ? "flex" : "hidden"
      } fixed inset-0 items-center justify-center z-50`}
    >
      <div className="bg-black opacity-50 fixed inset-0"></div>
      <div className="bg-white p-6 rounded-md z-10">
        <h2 className="text-2xl font-bold mb-4">Edit Budget</h2>
        <label className="block mb-2">Name:</label>
        <input
          type="text"
          name="name"
          value={editedBudget.name}
          onChange={handleInputChange}
          className="border border-gray-300 p-2 mb-4 w-full"
        />
        <label className="block mb-2">Amount:</label>
        <input
          type="number"
          name="amount"
          value={editedBudget.amount}
          onChange={handleInputChange}
          className="border border-gray-300 p-2 mb-4 w-full"
        />
        {/* Add more fields as needed */}
        <button
          onClick={handleSave}
          className="bg-blue-500 text-white px-4 py-2 mr-2 rounded"
        >
          Save
        </button>
        <button
          onClick={onClose}
          className="bg-gray-300 text-gray-700 px-4 py-2 rounded"
        >
          Cancel
        </button>
      </div>
    </div>
  );
};

export default EditBudgetModal;
