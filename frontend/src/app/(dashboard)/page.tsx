import MonthlyActivity from "@/components/chart/MonthlyActivity";
import MonthlyTarget from "@/components/chart/MonthlyTarget";
import { UserMetrics } from "@/components/chart/UserMetrics";

export default function Ecommerce() {
  return (
    <div className="grid grid-cols-12 gap-4 md:gap-6">
      <div className="col-span-12 space-y-6 xl:col-span-7">
        <UserMetrics />

        <MonthlyActivity />
      </div>
      <div className="col-span-12 xl:col-span-5">
        <MonthlyTarget />
      </div>
    </div>
  );
}