import json
from app.core.activity_processing import aggregate_logs, extract_date_and_activities, date_entry_managment, merge_activities, normalize_raw_data
from utils.time_utils import compute_activities_time
import os

def save_json_array(arr, file_path):
    arr.sort(key=lambda x: next(iter(x)))
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(arr, f, indent=2, ensure_ascii=False)

def load_json_array(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_log_line(data, file_path):
    arr = load_json_array(file_path)
    date, new_activities = extract_date_and_activities(data)
    activities = date_entry_managment(arr, date)

    merge_activities(activities, new_activities)

    compute_activities_time(activities)

    save_json_array(arr, file_path)

def  add_aggregated_data(SOURCE_FILE,DESTINATION_FILE):

    if not os.path.exists(SOURCE_FILE):
            return

    raw_data = load_json_array(SOURCE_FILE)
    if not raw_data:
        return

    cleaned_data = normalize_raw_data(raw_data)
    final_result = aggregate_logs(cleaned_data)

    save_json_array(final_result, DESTINATION_FILE )