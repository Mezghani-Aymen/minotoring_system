
def get_filename(file_type , date) :
    """
    Return dynamic file name based on type.
    
    file_type: "raw", "aggregated", "archive"
    """
    
    if file_type == "raw":
        return f"raw_{date}.json"
    elif file_type == "aggregated":
        return f"aggregated_{date}.json"
    elif file_type == "archive":
        return f"archive_raw_{date}.json"
    else:
        raise ValueError(f"Unknown file type: {file_type}")
