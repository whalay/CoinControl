import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import EditBudgetModal from "../components/EditBudgetModal";

const DashBoardBudget = () => {
  const [budgetData, setBudgetData] = useState([]);
  const [editBudget, setEditBudget] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false); // New state for the modal

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
          console.log(response.data.data);
          setBudgetData(response.data.data.data);
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

  const handleDeleteBudget = async (budgetId) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this budget?"
    );

    if (!confirmed) {
      return; // User canceled the deletion
    }
    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.delete(
        `${import.meta.env.VITE_APP_URL}/budgets/${budgetId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.status === 200) {
        // Remove the deleted budget from the local state
        setBudgetData((prevData) =>
          prevData.filter((budget) => budget.id !== budgetId)
        );
      } else {
        throw new Error("Failed to delete budget");
      }
    } catch (error) {
      console.error("Error deleting budget:", error);
      // Handle the error as needed
    }
  };

  const handleEditBudget = (budget) => {
    console.log("Editing budget:", budget);

    setEditBudget(budget);
    setIsEditModalOpen(true); // Open the modal when editing a budget
  };

  const handleSaveEdit = async (updatedBudget) => {
    try {
      const token = localStorage.getItem("accessToken");
      const response = await axios.put(
        `${import.meta.env.VITE_APP_URL}/budgets/${updatedBudget.id}`,
        updatedBudget,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.status === 200) {
        // Update the local state with the edited budget
        setBudgetData((prevData) =>
          prevData.map((budget) =>
            budget.id === updatedBudget.id ? updatedBudget : budget
          )
        );
        alert("Budget updated successfully.");
      } else {
        throw new Error("Failed to update budget");
      }
    } catch (error) {
      console.error("Error updating budget:", error);
      alert("Failed to update budget. Please try again.");
    } finally {
      setEditBudget(null);
    }
  };

  return (
    <section className="p-6 rounded-md shadow-md mb-4">
      <h2 className="text-2xl font-semibold mb-4">Budget</h2>
      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">{error}</p>}
      <div className="flex flex-col md:flex-row justify-start gap-5">
        {Array.isArray(budgetData) && budgetData.length > 0 ? (
          budgetData.map((budget) => (
            <div
              className="rounded-md shadow-md p-5 w-2xl space-y-5"
              key={budget.id}
            >
              <Link
                to={`${budget.id}`}
                className="text-blue-500 hover:underline"
              >
                <h6 className="text-4xl font-semibold mb-1">{budget.name}</h6>
                <p className="font-semibold text-xl">${budget.amount}</p>
                <p>{budget.date_created}</p>
              </Link>
              <div className="my-2 space-x-10 text-xl">
                {" "}
                <button onClick={() => handleDeleteBudget(budget.id)}>
                  Delete
                </button>
                <button onClick={() => handleEditBudget(budget)}>Edit</button>
              </div>
            </div>
          ))
        ) : (
          <p>No budget data available.</p>
        )}
        <div>
          {editBudget && (
            <EditBudgetModal
              budget={editBudget}
              isOpen={isEditModalOpen}
              onSave={handleSaveEdit}
              // onClose={() => setEditBudget(null)}
              onClose={() => setIsEditModalOpen(false)} // Close the modal on cancel or after saving
            />
          )}
        </div>
      </div>
    </section>
  );
};

export default DashBoardBudget;
