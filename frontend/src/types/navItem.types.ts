export type NavItem = {
    name: string;
    icon: React.ElementType;
    path?: string;
    subItems?: { name: string; path: string; pro?: boolean; new?: boolean }[];
};