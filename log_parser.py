def parse_log_file(log_path):
    """
    Parses the log file and returns a list of log entries.
    Each entry is a dictionary with 'user_id' and 'file_accessed'.
    """
    log_entries = []
    with open(log_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                user_id, file_accessed = parts
                log_entries.append({
                    'user_id': user_id,
                    'file_accessed': file_accessed
                })
    return log_entries