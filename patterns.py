from safeeval import SafeEval
import re

class PatternMatcher:
    """Class to handle loading patterns and matching them to user statistics."""
    
    def __init__(self, pattern_path):
        self.pattern_path = pattern_path
        self.patterns = list()

    def load_patterns(self):
        """Loads patterns from the file."""
        self.patterns = []
        with open(self.pattern_path, 'r') as file:
            for line in file:
                condition, description = line.strip().split(',', maxsplit=1)

                self.patterns.append({
                    'condition': condition,
                    'description': description
                })

        return self.patterns

    def match(self, user_stats):
        """Matches patterns against the user statistics."""
        matches = []
        safe_eval = SafeEval()

        for user_id, stats in user_stats.items():
            file_access_counts = stats['file_access_counts']

            for pattern in self.patterns:
                condition = pattern['condition']
                description = pattern['description']

                files_in_condition = self.__extract_files_from_condition(condition)

                # skip processing if the user does not have any record accessing the file
                if not any(file in file_access_counts for file in files_in_condition):
                    continue 

                if safe_eval.safeEval(condition, file_access_counts):
                    matches.append({
                        'user_id': user_id,
                        'message': description
                    })

        return matches
    
    def __extract_files_from_condition(self, condition: str) -> set:
        """
        Extracts file references (e.g., FileA, FileB) from a condition string.
        Returns a set of file names found in the condition.
        """

        # Assuming file references are like 'FileA', 'FileB', etc.
        # This regex looks for words starting with 'File' followed by a letter or number.
        file_pattern = r'\bFile[A-Z0-9]+\b'
        
        # Find all file references in the condition
        return set(re.findall(file_pattern, condition))


