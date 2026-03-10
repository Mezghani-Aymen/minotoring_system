import { NavItem } from "@/types/navItem.types";
import {
  GridIcon,
  Settings
} from "@/icons";

export const navItems: NavItem[] = [
  {
    icon: GridIcon,
    name: "Dashboard",
    path: "/dashboard",
  },
  {
    icon: Settings,
    name: "Settings",
    path: "/settings",
  }
];
