from app.config.settings import INTERACTION_SCHEMA
from collections import defaultdict
from utils.time_utils import parse_duration_to_seconds, seconds_to_hms


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
                        "primary": monitor_info[1],
                        "extra": interaction_data.get("extra") or []
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
        extra = new_act.get("extra") 

        for act in activities:
            if act["context"] == context:
                merge_values(act["value"], values)
                if extra:
                    act.setdefault("extra", []).extend(extra)
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
        extra = new.get("extra")

        for exist in existing:
            if exist["application"] == app and exist["topic"] == topic:
                if ts not in exist["timestamps"]:
                    exist["timestamps"].append(ts)
                exist["timestamps"].sort()
                if extra:
                    exist.setdefault("extra", []).extend(extra)
                break
        else:
            existing.append({
                "monitor": new.get("monitor"),
                "primary": new.get("primary"),
                "application": app,
                "topic": topic,
                "timestamps": [ts],
                "extra": extra or []
            })


def parse_log_monitor(monitor_info):
    device = monitor_info.get("device")
    primary = monitor_info.get("primary")
    return device.replace("\\\\.\\", "").lower(), primary

def normalize_raw_data(data):
    """
    Flattens raw data into clean list of entries.
    Handles:
    - Date-key dictionaries
    - Context-based structure
    - Direct entries
    """
    normalized = []

    if not isinstance(data, list):
        return []

    for item in data:

        # Case 1: Date-key wrapper
        # { "2026-02-12": [ ... ] }
        if isinstance(item, dict) and len(item) == 1:
            date_key = next(iter(item))
            inner_list = item.get(date_key, [])

            for ctx_block in inner_list:
                context_name = ctx_block.get("context", "Unknown")
                values = ctx_block.get("value", [])

                for v in values:
                    v["_context"] = context_name
                    v["_date"] = date_key
                    normalized.append(v)

        # Case 2: Already flattened context
        elif "context" in item:
            context_name = item["context"]
            values = item.get("value", [])

            for v in values:
                v["_context"] = context_name
                normalized.append(v)

        else:
            normalized.append(item)

    return normalized


def aggregate_logs(normalized_data) :
    """
    Groups data by Context -> App.
    Sums time and merges topics.
    """
    # Structure: context -> app -> { stats }
    grouped = defaultdict(lambda: {
        "apps": defaultdict(lambda: {
            "topics": set(),
            "monitor": None,
            "total_seconds": 0
        }),
        "context_total_seconds": 0
    })

    for entry in normalized_data:
        # 1. Extract Fields
        context = entry.get("_context") or entry.get("context", "Unknown")
        app = entry.get("app") or entry.get("application", "Unknown")
        time_str = entry.get("total_time", "00:00:00")
        topics = entry.get("topic", [])
        monitor = entry.get("monitor")
        is_primary = entry.get("primary", False)

        if isinstance(topics, str): topics = [topics]

        # 2. Calculate
        seconds = parse_duration_to_seconds(time_str)

        # 3. Aggregate
        ctx_ref = grouped[context]
        app_ref = ctx_ref["apps"][app]

        app_ref["total_seconds"] += seconds
        app_ref["topics"].update(topics)
        ctx_ref["context_total_seconds"] += seconds

        # Logic: Update monitor if primary, or if we don't have one yet
        if is_primary or (monitor and not app_ref["monitor"]):
            app_ref["monitor"] = monitor

    # 4. Format Output
    final_output = []
    for ctx_name, ctx_data in grouped.items():
        apps_list = []
        for app_name, app_data in ctx_data["apps"].items():
            app_obj = {
                "app": app_name,
                "topic": sorted(list(app_data["topics"])),
                # "total_time": format_seconds_to_hms(app_data["total_seconds"]) # Optional: add app total
            }
            if app_data["monitor"]:
                app_obj["monitor"] = app_data["monitor"]
            apps_list.append(app_obj)

        final_output.append({
            "context": ctx_name,
            "value": apps_list,
            "total_time": seconds_to_hms(ctx_data["context_total_seconds"])
        })

    return final_output