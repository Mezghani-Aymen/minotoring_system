from config import INTERACTION_SCHEMA

def parse_log_interaction(interaction: str, schema: list = INTERACTION_SCHEMA):

    if not interaction or not isinstance(interaction, str):
        return None

    parts = [p.strip() for p in interaction.split(" - ") if p.strip()]

    if len(parts) < len(schema):
        parts = parts + [None] * (len(schema) - len(parts))

    values = parts[:len(schema)]
    data = dict(zip(schema, values))

    if len(parts) > len(schema):
        data["extra"] = parts[len(schema):]

    data["context"] = data["context"].split(".", 1)[0]

    return data


def parse_log_line(interaction_info, monitor_info):

    interaction_data = {}
    for key in INTERACTION_SCHEMA:
        interaction_data[key] = interaction_info.get(key)

    if "extra" in interaction_info:
        interaction_data["extra"] = interaction_info["extra"]

    date = interaction_data.get("date")

    return  {
        date: [
            {
                "context": interaction_data.get("context"),
                "value": [
                    {
                        "timestamp": interaction_data.get("timestamp"),
                        "application": interaction_data.get("application"),
                        "topic": interaction_data.get("topic"),
                        "monitor": monitor_info[0],
                        "primary": monitor_info[1]
                    }
                ]
            }
        ]
    }


def extract_date_and_activities(data):
    date = next(iter(data))
    return date, data[date]


def date_entry_managment(arr, date):
    """
    Create or get date entry from arr
    """
    for item in arr:
        if date in item:
            return item[date]

    activities = []
    arr.append({date: activities})
    return activities


def merge_activities(activities, new_activities):
    for new_act in new_activities:
        context = new_act["context"]
        values = new_act["value"]

        for act in activities:
            if act["context"] == context:
                merge_values(act["value"], values)
                break
        else:
            normalize_timestamps(values)
            activities.append(new_act)


def normalize_timestamps(values):
    """ Convert timestamps to list """
    for v in values:
        v["timestamps"] = [v.pop("timestamp")]


def merge_values(existing, incoming):
    for new in incoming:
        app = new["application"]
        topic = new["topic"]
        ts = new["timestamp"]

        for exist in existing:
            if exist["application"] == app and exist["topic"] == topic:
                # add timestamp only if it doesn't exist
                if ts not in exist["timestamps"]:
                    exist["timestamps"].append(ts)

                # keep timestamps sorted
                exist["timestamps"].sort()
                break
        else:
            existing.append({
                "monitor": new.get("monitor"),
                "primary": new.get("primary"),
                "application": app,
                "topic": topic,
                "timestamps": [ts]
            })


def parse_log_monitor(monitor_info):
    device = monitor_info.get("device")
    primary = monitor_info.get("primary")
    return device.replace("\\\\.\\", "").lower(), primary