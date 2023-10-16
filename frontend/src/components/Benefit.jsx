import benefit from "../assets/images/benefit-bg.png";
// import checkmark from "../assets/images/checkmark.png";

const Benefit = () => {
  return (
    // <div className="mt-[400px] md:mt-0 h-screen flex md:flex-col flex-wrap items-center   ">
    <div className="h-screen sm:mt-[350px] md:mt-0 flex items-center justify-center gap-20 md:flex-row flex-col ">
      <div className="flex-1/2 w-full">
        <img src={benefit} alt="" className="w-fit" />
      </div>

      <div className="flex flex-col flex-1/2 md:pr-20  md:items-stretch space-y-10">
        <h1 className="text-3xl md:text-5xl font-bold">What benefit will you get?</h1>
        <ul className="text-xl md:text-2xl space-y-5">
          <li>Finance Awareness</li>
          <li>Expense Tracking</li>
          <li>Budgeting Tracking</li>
          <li>Financial Visualization and Reporting</li>
          <li>Financial Goal Achievement</li>
        </ul>
      </div>
    </div>
  );
};

export default Benefit;
