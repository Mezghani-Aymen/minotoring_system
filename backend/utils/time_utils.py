from datetime import datetime
from app.config.settings import IDLE_THRESHOLD_SECONDS

def now(format = "object"):
    currentDateTime= datetime.now()

    if format == "string":
        return currentDateTime.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return currentDateTime


def current_date(format = "object"):
    currentDate = now("object").date()

    if format =="string":
        return currentDate.strftime("%Y-%m-%d")
    else:
        return currentDate


def current_time(format = "object"):
    currentTime = now("object").time()
    if format =="string":
        return currentTime.strftime("%H:%M:%S")
    else:
        return currentTime



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
            value["total_time"] = seconds_to_hms(total_seconds)