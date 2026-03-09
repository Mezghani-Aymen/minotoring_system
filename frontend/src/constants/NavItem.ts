import { NavItem } from "@/types/navItem.types";
import {
  GridIcon,
  CalenderIcon
} from "@/icons";

export const navItems: NavItem[] = [
  {
    icon: GridIcon,
    name: "Dashboard",
    path: "/dashboard",
  },
  {
    icon: CalenderIcon,
    name: "Calendar",
    path: "/calendar",
  }
];
