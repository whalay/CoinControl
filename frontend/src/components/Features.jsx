import budget from "../assets/images/budget-icon.png";
import expense from "../assets/images/expense-icon.png";
import report from "../assets/images/report-icon.png";

const Features = () => {
  return (
  <div className=" h-screen">
      <div className=" bg-slate-200 absolute left-0  w-full ">
      <div className=" md:px-20 px-5 my-20 space-y-16 flex flex-col justify-end items-stretch text-center">
        <div className="space-y-5">
          <h4 className="text-xl">FEATURES</h4>
          <h2 className="text-4xl font-bold">Our Special Features</h2>
          <p>
            Powerful metrics to better understand your finances are right at
            your fingertips once you start working with them!
          </p>
        </div>
        <div className="flex flex-col md:flex-row  justify-between items-center gap-10">
          <div className="bg-[#DFE2E5] border rounded-3xl">
            <div className="m-10 flex-col flex items-center text-center space-y-5">
              <div className="bg-[#1A194D] h-16 w-16 border-none rounded-full ">
              
                <img src={expense} alt="" className="p-2" />
              </div>{" "}
              <h3 className="font-bold">Expense Tracking</h3>
              <p className="">
                Effortlessly track your expenses and categorize them for better
                finacial management
              </p>
            </div>
          </div>
          <div className="bg-[#DFE2E5] border rounded-3xl">
            <div className="m-10 flex-col flex items-center text-center space-y-5">
            <div className="bg-[#EE6338] h-16 w-16 border-none rounded-full ">
              <img src={budget} alt="" className="p-2"/>
              </div>
            
              <h3>Budgeting</h3>
              <p>
                Effortlessly track your expenses and categorize them for better
                finacial management
              </p>
            </div>
          </div>
          <div className="bg-[#DFE2E5] border rounded-3xl">
            <div className="m-10 flex-col flex items-center text-center space-y-5">
            <div className="bg-[#1FB141] h-16 w-16 border-none rounded-full ">
              <img src={report} alt="" className="p-2"/>
              </div>
              <h3>Reports</h3>
              <p>
                Effortlessly track your expenses and categorize them for better
                finacial management
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>

  );
};

export default Features;
