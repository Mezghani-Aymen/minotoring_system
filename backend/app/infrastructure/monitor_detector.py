import win32api
import win32con
from app.infrastructure.window_utils import get_foreground_hwnd

def get_window_monitor():
    hwnd = get_foreground_hwnd()
    if not hwnd:
        return None

    monitor = win32api.MonitorFromWindow(
        hwnd, win32con.MONITOR_DEFAULTTONEAREST
    )
    info = win32api.GetMonitorInfo(monitor)

    return {
        "device": info["Device"],
        "primary": info["Flags"] == 1,
    }