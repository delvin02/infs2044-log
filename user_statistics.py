from collections import defaultdict

class UserStatistics:
    """Class to handle computation of user statistics."""
    
    def __init__(self, log_entries):
        self.log_entries = log_entries
        self.user_stats = defaultdict(lambda: {
        'files_accessed': set(),
        'file_access_counts': defaultdict(int)
        })
    
        
    def compute(self):
        """
        Computes statistics for each user.
        Returns a dictionary with user IDs as keys.
        Each value is a dictionary containing:
        - 'files_accessed': set of files accessed
        - 'file_access_counts': dict of file access counts
        """

        for entry in self.log_entries:
            user_id = entry['user_id']
            file_accessed = entry['file_accessed']

            self.user_stats[user_id]['files_accessed'].add(file_accessed)
            self.user_stats[user_id]['file_access_counts'][file_accessed] += 1

        return self.user_stats