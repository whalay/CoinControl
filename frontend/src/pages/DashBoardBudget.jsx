
const DashBoardBudget = () => {
  return (
    <section className="p-6 rounded-md shadow-md mb-4">
          <h2 className="text-2xl font-semibold mb-4">Budget</h2>
          <div className="flex flex-col md:flex-row justify-start gap-5">
            <div className="rounded-md shadow-md p-2">
              <h6 className="text-xl font-semibold mb-1">$200,000</h6>
              <p className="font-semibold text-md">school fees</p>
            </div>

            <div className="rounded-md shadow-md p-2">
              <h6 className="text-xl font-semibold mb-1">$200,000</h6>
              <p className="font-semibold text-md">school fees</p>
            </div>
            <div className="rounded-md shadow-md p-2">
              <h6 className="text-xl font-semibold mb-1">$200,000</h6>
              <p className="font-semibold text-md">school fees</p>
            </div>
          </div>
        </section>
  )
}

export default DashBoardBudget