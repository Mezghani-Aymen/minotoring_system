"use client";
import { BoxIconLine, GroupIcon } from "@/icons";
import { MetricItem } from "@/components/ui/MetricItem";

export const UserMetrics = () => {
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:gap-6">
      <MetricItem
        title="Work Sessions"
        value="---------"
        icon={<GroupIcon className="text-gray-800 size-6 dark:text-white/90" />}
        trend="up"
        percentage="11.01%"
      />

      <MetricItem
        title="Orders"
        value="5,359"
        icon={<BoxIconLine className="text-gray-800 dark:text-white/90" />}
        trend="down"
        percentage="9.05%"
      />
    </div>
  );
};