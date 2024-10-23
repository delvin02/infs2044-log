from safeeval import SafeEval
import re

def load_patterns(pattern_path) -> list:
    patterns = []
    with open(pattern_path, 'r') as file:
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

            files_in_condition = extract_files_from_condition(condition)

            if not any(file in file_access_counts for file in files_in_condition):
                continue 

            if safe_eval.safeEval(condition, file_access_counts):
                matches.append({
                    'user_id': user_id,
                    'message': description
                })

    return matches

def extract_files_from_condition(condition: str) -> set:
    """
    Extracts file references (e.g., FileA, FileB) from a condition string.
    Returns a set of file names found in the condition.
    """
    
    # Assuming file references are like 'FileA', 'FileB', etc.
    # This regex looks for words starting with 'File' followed by a letter or number.
    file_pattern = r'\bFile[A-Z0-9]+\b'
    
    # Find all file references in the condition
    return set(re.findall(file_pattern, condition))
