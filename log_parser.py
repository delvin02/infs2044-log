class LogParser:
    """ Class to handle parsing of the log file"""

    def __init__(self, log_path):
        self.log_path = log_path
    
    def parse(self):
        log_entries = []
        with open(self.log_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    user_id, file_accessed = parts
                    log_entries.append({
                        'user_id': user_id,
                        'file_accessed': file_accessed
                    })
        return log_entries
