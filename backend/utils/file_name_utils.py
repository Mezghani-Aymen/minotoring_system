from utils.time_utils import current_date

def get_filename(file_type) :
    """
    Return dynamic file name based on type.
    
    file_type: "raw", "aggregated", "archive"
    """
    date_str = current_date()

    if file_type == "raw":
        return f"raw_{date_str}.json"
    elif file_type == "aggregated":
        return f"aggregated_{date_str}.json"
    elif file_type == "archive":
        return f"archive_raw_{date_str}.json"
    else:
        raise ValueError(f"Unknown file type: {file_type}")
