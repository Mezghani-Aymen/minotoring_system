'use client'
import { useState } from 'react';

// --- Shared Assets ---
const CheckIcon = () => (
    <svg className="w-3.5 h-3.5 text-brand-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3.5" strokeLinecap="round" strokeLinejoin="round">
        <polyline points="20 6 9 17 4 12" />
    </svg>
);

const CrossIcon = () => (
    <svg className="w-3.5 h-3.5 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3.5" strokeLinecap="round" strokeLinejoin="round">
        <line x1="18" y1="6" x2="6" y2="18" />
        <line x1="6" y1="6" x2="18" y2="18" />
    </svg>
);

const SettingToggle = ({ initialState = true }: { initialState?: boolean }) => {
    const [isOn, setIsOn] = useState(initialState);
    return (
        <button
            type="button"
            onClick={() => setIsOn(!isOn)}
            className={`relative inline-flex h-8 w-13 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2 dark:focus:ring-offset-gray-900 ${isOn ? 'bg-brand-500' : 'bg-gray-200 dark:bg-gray-800'
                }`}
        >
            <span className={`inline-flex h-6 w-6 transform items-center justify-center rounded-sm bg-white transition-transform duration-200 ease-in-out shadow-sm ${isOn ? 'translate-x-[1.4rem]' : 'translate-x-[0.25rem]'
                }`}>
                {isOn ? <CheckIcon /> : <CrossIcon />}
            </span>
        </button>
    );
};

export default SettingToggle;
