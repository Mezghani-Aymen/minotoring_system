import ctypes
import win32gui, win32process, psutil
from app.config.settings import AFK_THRESHOLD_SECONDS
from utils.time_utils import current_date, current_time
from app.infrastructure.window_utils import get_foreground_hwnd


def check_user_activity():
    idle_seconds = get_afk_time_seconds()

    if idle_seconds >= AFK_THRESHOLD_SECONDS:
        return True

    return False


def get_afk_time_seconds():
    class _LASTINPUTINFO(ctypes.Structure):
        _fields_ = [
            ("cbSize", ctypes.c_uint),
            ("dwTime", ctypes.c_uint),
        ]

    info = _LASTINPUTINFO()
    info.cbSize = ctypes.sizeof(_LASTINPUTINFO)

    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(info)):
        millis = ctypes.windll.kernel32.GetTickCount() - info.dwTime
        return int(millis / 1000)

    return 0


def parse_window_title(hwnd):
    raw_title = win32gui.GetWindowText(hwnd)

    if not raw_title or raw_title == "Program Manager":
        return "Desktop", "Desktop"

    parts = raw_title.split()

    topic_name = parts[0]
    program_name = " ".join(parts[-3:]) if len(parts) >= 3 else raw_title

    return program_name, topic_name


def collect_active_window_log():
    hwnd = get_foreground_hwnd()
    if not hwnd:
        return None

    window_title, topic_name = parse_window_title(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    process_name = psutil.Process(pid).name()
    log_line = f"{current_date("string")} - {current_time("string")} - {window_title} - {process_name} - {topic_name}"

    return log_line