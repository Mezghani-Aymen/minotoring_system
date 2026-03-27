import { NavItem } from "@/types/navItem.types";
import {
  GridIcon,
  Settings
} from "@/icons";

export const navItems: NavItem[] = [
  {
    icon: GridIcon,
    name: "Dashboard",
    path: "/",
  },
  {
    icon: Settings,
    name: "Settings",
    subItems: [{ name: "General", path: "/settings/general" }, { name: "Notification", path: "/settings/notification" }],
  }
];
