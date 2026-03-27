import { invoke } from "@tauri-apps/api/core";
import { useState, useEffect } from "react";

const StatusBadge = () => {
    const [isRunning, setIsRunning] = useState(false);

    useEffect(() => {
        const checkStatus = async () => {
            if (typeof window === "undefined") return;
            try {
                const status = await invoke<boolean>("is_python_running");
                setIsRunning(status);
            } catch (err) {
                setIsRunning(false);
            }
        };

        checkStatus();
        const interval = setInterval(checkStatus, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="flex items-center gap-2 px-3 py-1 bg-gray-100 rounded-full dark:bg-white/5">
            <div
                className={`w-2 h-2 rounded-full ${isRunning ? "bg-green-500 animate-pulse" : "bg-gray-400"
                    }`}
            ></div>
            <span className="text-xs font-medium text-gray-600 dark:text-gray-400">
                {isRunning ? "Tracking Active" : "Tracking Inactive"}
            </span>
        </div>
    );
};

export default StatusBadge