import os
from pathlib  import Path

AFK_THRESHOLD_SECONDS = 60  # 1 minute
INTERVAL = 1  # seconds
IDLE_THRESHOLD_SECONDS = 5
INTERACTION_SCHEMA = ["date", "timestamp", "application", "context" , "topic"]
OPTIMIZIED_ATTRIBUTES_SCHEMA = ["date", "total_time", "application", "context" , "monitor"]
MERGED_ATTRIBUTES_SCHEMA = ["date", "total_time", "application", "context" , "monitor","topic","extra","primary"]
AFK_ALERT_SHOWN = False
RAW_FILE_PATH = Path(os.getenv("RAW_FILE_PATH", "./data/raw/"))
AGGREGATED_FILE_PATH = Path(os.getenv("AGGREGATED_FILE_PATH", "./data/aggregated/"))

# Ensure directories exist
RAW_FILE_PATH.mkdir(parents=True, exist_ok=True)
AGGREGATED_FILE_PATH.mkdir(parents=True, exist_ok=True)