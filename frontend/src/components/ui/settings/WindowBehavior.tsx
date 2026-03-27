'use client'
import { useState } from "react";

// Custom Radio Button
const RadioBtn = ({ checked }: { checked: boolean }) => (
    <div className="pt-1 shrink-0 cursor-pointer">
        {checked ? (
            <div className="w-5 h-5 rounded-full border-2 border-brand-500 flex items-center justify-center p-0.5">
                <div className="w-full h-full rounded-full bg-brand-500"></div>
            </div>
        ) : (
            <div className="w-5 h-5 rounded-full border-2 border-gray-300 bg-white dark:border-gray-700 dark:bg-gray-800 hover:border-brand-500 dark:hover:border-brand-500 transition-colors"></div>
        )}
    </div>
);


export default function WindowBehavior() {
    const [closeBehavior, setCloseBehavior] = useState('exit');

    return (
        <div className="mb-10">
            <div className="text-[11px] font-extrabold text-gray-500 dark:text-gray-400 tracking-widest uppercase mb-4">
                Close Window
            </div>

            {/* Option A: Minimize */}
            <div
                className="flex items-start gap-4 mb-6 cursor-pointer"
                onClick={() => setCloseBehavior('minimize')}
            >
                <RadioBtn checked={closeBehavior === 'minimize'} />
                <div className="flex-1">
                    <div className="flex items-center gap-3 mb-1">
                        <h2 className="text-lg font-bold">Minimize to system tray</h2>
                        <span className="bg-gray-100 dark:bg-gray-800 text-[10px] font-bold text-gray-500 dark:text-gray-400 px-2 py-0.5 rounded-sm tracking-[0.08em] uppercase">
                            Recommended
                        </span>
                    </div>
                    <p className="text-gray-500 dark:text-gray-400 text-sm leading-relaxed">
                        Monitoring System will stay running, which ensures you receive alerts faster and keeps monitoring your system automatically.
                    </p>
                </div>
            </div>

            {/* Option B: Exit Application */}
            <div
                className="flex items-center gap-4 cursor-pointer"
                onClick={() => setCloseBehavior('exit')}
            >
                <RadioBtn checked={closeBehavior === 'exit'} />
                <h2 className="text-lg font-bold">Exit application</h2>
            </div>
        </div>
    );
}