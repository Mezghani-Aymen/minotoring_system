AFK_THRESHOLD_SECONDS = 60  # 1 minute
INTERVAL = 1  # seconds
MONITORING_FILE = "monitoring.json"
VISUALISATION_FILE= "visualisation.json"
IDLE_THRESHOLD_SECONDS = 5
INTERACTION_SCHEMA = ["date", "timestamp", "application", "context" , "topic"]
OPTIMIZIED_ATTRIBUTES_SCHEMA = ["date", "total_time", "application", "context" , "monitor"]
MERGED_ATTRIBUTES_SCHEMA = ["date", "total_time", "application", "context" , "monitor","topic","extra","primary"]
# ATTRIBUTES_SCHEMA = {
#     "date": "date",
#     "context": "context",
#     "value": "value",
#     "timestamp": "timestamp",
#     "application": "application",
#     "topic": "topic",
#     "monitor": "monitor",
#     "primary": "primary",
#     "extra": "extra"
# }