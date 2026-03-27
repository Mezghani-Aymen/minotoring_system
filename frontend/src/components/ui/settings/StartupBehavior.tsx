import SettingToggle from "./SettingToggle";

export default function StartupBehavior() {
    return (
        <div className="mb-10">
            <div className="text-[11px] font-extrabold text-gray-500 dark:text-gray-400 tracking-widest uppercase mb-4">
                Startup Behavior
            </div>
            <div className="flex items-start justify-between">
                <div className="flex-1 pr-8">
                    <div className="flex items-center gap-3 mb-1.5">
                        <h2 className="text-lg font-bold">Open Monitoring System on startup</h2>
                        <span className="bg-gray-100 dark:bg-gray-800 text-[10px] font-bold text-gray-500 dark:text-gray-400 px-2 py-0.5 rounded-sm tracking-[0.08em] uppercase">
                            Recommended
                        </span>
                    </div>
                    <p className="text-gray-500 dark:text-gray-400 text-sm leading-relaxed">
                        Monitoring System will run in your system tray when your computer starts so your system can be monitored continuously.
                    </p>
                </div>
                <div className="pt-1">
                    <SettingToggle initialState={true} />
                </div>
            </div>
        </div>
    );
}