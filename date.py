from datetime import datetime
from config import IDLE_THRESHOLD_SECONDS

def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_date():
    return datetime.now().strftime("%Y-%m-%d")


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def calculate_active_time(timestamps, idle_threshold=IDLE_THRESHOLD_SECONDS):
    if len(timestamps) < 2:
        return [], 0

    times = [datetime.strptime(t, "%H:%M:%S") for t in timestamps]

    sessions = []
    current_session = 0

    for prev, curr in zip(times, times[1:]):
        delta = (curr - prev).total_seconds()

        if delta <= idle_threshold:
            current_session += delta
        else:
            sessions.append(current_session)
            current_session = 0

    sessions.append(current_session)
    return sessions, int(sum(sessions))

def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

def compute_activities_time(activities, idle_threshold=IDLE_THRESHOLD_SECONDS):
    """
    For each activity value, compute total active time
    from timestamps and store it in 'total_time'
    """
    for activity in activities:
        for value in activity["value"]:
            timestamps = value.get("timestamps", [])

            _, total_seconds = calculate_active_time(
                timestamps,
                idle_threshold
            )
            # TODO: every 60 seconds remove 60 lines from timestamps to avoid memory overload
            value["total_time"] = seconds_to_hms(total_seconds)