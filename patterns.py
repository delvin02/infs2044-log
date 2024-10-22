from safeeval import SafeEval
from collections import defaultdict
import re
# define pattern priority for sorting
pattern_priority = {
    'File A and B or C were accessed': 1,
    'File A was accessed': 2,
    'File A was accessed twice': 4,
    'File D was accessed': 3,
    'All three files were accessed': 6
}

def load_patterns(pattern_path) -> list:
    patterns = []
    with open(pattern_path, 'r') as file:
        next(file)
        for line in file:
            condition, description = line.strip().split(',', maxsplit=1)

            patterns.append({
                'condition': condition,
                'description': description
            })

    return patterns

def match_patterns(user_stats, patterns):
    """
    Matches users against patterns by evaluating conditions.
    Returns a list of matches in the format:
    [{'user_id': ..., 'message': ...}, ...], sorted by priority per user.
    """
    matches = []
    safe_eval = SafeEval()

    for user_id, stats in user_stats.items():
        file_access_counts = stats['file_access_counts']

        for pattern in patterns:
            condition = pattern['condition']
            description = pattern['description']

            # Extract the file names from the condition using regex
            file_names_in_condition = re.findall(r'\bFile\w+\b', condition)

            # Ensure all file names in the condition are in file_access_counts
            if not all(file in file_access_counts for file in file_names_in_condition):
                continue  # Skip condition if the user hasn't accessed the required files

            # Evaluate the condition
            if safe_eval.safeEval(condition, file_access_counts):
                matches.append({
                    'user_id': user_id,
                    'message': description
                })

    # Sort all matches globally by pattern priority
    sorted_matches = sorted(
        matches,
        key=lambda match: pattern_priority.get(match['message'], float('inf'))
    )

    return sorted_matches
