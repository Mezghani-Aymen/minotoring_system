import win32gui, win32process, psutil
from date import current_date, current_time
from window_utils import get_foreground_hwnd


# TODO: Add mousse tracing / AFK detection

def parse_window_title(hwnd):
    title = win32gui.GetWindowText(hwnd).split()
    print ('title: ' + title)
    topic_name = title[0]
    program_name = ' '.join(title[-3:])

    return program_name, topic_name

def collect_active_window_log():
    hwnd = get_foreground_hwnd()
    print ("hwnd: " + str(hwnd))
    if not hwnd:
        return None

    window_title, topic_name = parse_window_title(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    process_name = psutil.Process(pid).name()
    log_line = f"{current_date()} - {current_time()} - {window_title} - {process_name} - {topic_name}"

    return log_line