import time
from app.config.settings import AFK_ALERT_SHOWN, INTERVAL
from app.core.activity_processing import parse_log_line, parse_log_interaction , parse_log_monitor
from app.storage.json_repository import  add_log_line ,add_aggregated_data
from app.infrastructure.monitor_detector import get_window_monitor
from app.infrastructure.activity_collector import check_user_activity, collect_active_window_log
from utils.date_utils import get_previous_day, current_date
from utils.file_name_utils import get_filename
from services.notification import notify

if __name__ == "__main__":
    # TODO: Add prodectivity detection, conception, analysis
    # TODO: Add background app monitoring (like youtube videos , music players etc)
    # TODO: Add dashboard for visualizations and reports 
    # TODO: Add controll access to pc ( block certain apps / websites ) [firewall rules ? blocking process (can't read-write-exe) ? ]
    # TODO: Add AI assistant for help with tasks , scheduling , reminders , pressesion about progress about user skills level etc.
    # TODO: Add AI controller, guider [optional].
    # TODO: Add closing apps wwhen are used too much time. ( exammple : playing lol with it spend 2H , close it and block it for 24H )
    # TODO: Add more detailed logging ( keystrokes , mouse movements , clicks etc ) [optional].
    # TODO: Add notifications and alerts for user about productivity , time spent on certain apps/websites etc.
    # TODO: [Part league of legends] Add detection when user is in champion select / in game / in lobby etc. [optional].

    try:

        date = current_date()
        RAW_FILE = get_filename("raw", date)

        while True:

            new_date = current_date()
            if new_date != date:

                previous_raw_file = RAW_FILE
                aggregated_file = get_filename("aggregated", date)

                add_aggregated_data(previous_raw_file, aggregated_file)

                date = new_date
                RAW_FILE = get_filename("raw", date)

            AFK_status= check_user_activity()

            if not AFK_status:
                AFK_ALERT_SHOWN = False 

                monitor_info = get_window_monitor()
                interaction = collect_active_window_log()

                if not interaction or not monitor_info:
                    time.sleep(INTERVAL)
                    continue

                parsed = parse_log_interaction(interaction)
                if not parsed:
                    time.sleep(INTERVAL)
                    continue

                monitor = parse_log_monitor(monitor_info)
                if not monitor:
                    time.sleep(INTERVAL)
                    continue

                log_data = parse_log_line(parsed, monitor)
                add_log_line(log_data,RAW_FILE )

                time.sleep(INTERVAL)
            else :
               if not AFK_ALERT_SHOWN:
                notify("Monitoring System Stopped", "User is AFK!")
                AFK_ALERT_SHOWN = True
            
    except Exception as e:
        notify("Monitoring System Stoped", f"An error occurred: {e}")