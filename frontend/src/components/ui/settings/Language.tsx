const DropdownCaret = () => (
    <svg className="w-5 h-5 text-gray-500 dark:text-gray-400 fill-current" viewBox="0 0 24 24">
        <path d="M7 10l5 5 5-5z" />
    </svg>
);

export default function LanguageSettings() {
    return (
        <div className="mb-10">
            <div className="text-[11px] font-extrabold text-gray-500 tracking-widest uppercase mb-3 dark:text-gray-400">
                Language
            </div>
            <div className="relative w-full">
                <select className="w-full appearance-none rounded-xl border border-gray-200 bg-white px-4 py-3.5 text-sm text-gray-800 focus:border-brand-500 focus:outline-none focus:ring-1 focus:ring-brand-500 dark:border-gray-800 dark:bg-gray-dark dark:text-white/90 cursor-pointer">
                    <option>English (US)</option>
                    <option>Français</option>
                    <option>Español</option>
                </select>
                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-4">
                    <DropdownCaret />
                </div>
            </div>
        </div>
    );
}