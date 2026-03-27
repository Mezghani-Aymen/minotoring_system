export default function AppLanchSettings() {
    return (
        <div className="mb-10">
            <div className="text-[11px] font-extrabold text-gray-500 dark:text-gray-400 tracking-widest uppercase mb-4">
                App Launch
            </div>
            <div className="flex flex-col items-start">
                <h2 className="text-lg font-bold mb-1.5">Add Desktop Shortcut</h2>
                <p className="text-gray-500 dark:text-gray-400 text-sm leading-relaxed mb-6">
                    Add a desktop icon so you can jump right into Monitoring System.
                </p>
                <button className="px-6 py-2.5 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-brand-500 dark:hover:border-brand-500 text-gray-800 dark:text-white/90 font-bold rounded-lg transition-colors text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2 dark:focus:ring-offset-gray-900">
                    Add Desktop Shortcut
                </button>
            </div>
        </div>
    );
}