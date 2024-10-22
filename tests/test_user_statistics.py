import pytest
from user_statistics import compute_user_statistics

def test_compute_user_statistics():
    # sample log entries as input
    log_entries = [
        {'user_id': 'User1', 'file_accessed': 'FileA'},
        {'user_id': 'User2', 'file_accessed': 'FileA'},
        {'user_id': 'User1', 'file_accessed': 'FileB'},
        {'user_id': 'User1', 'file_accessed': 'FileA'},
        {'user_id': 'User3', 'file_accessed': 'FileD'},
        {'user_id': 'User1', 'file_accessed': 'FileC'}
    ]
    
    # Compute the statistics
    stats = compute_user_statistics(log_entries)
    
    # Verify the computed statistics
    expected = {
        'User1': {
            'files_accessed': {'FileA', 'FileB', 'FileC'},
            'file_access_counts': {'FileA': 2, 'FileB': 1, 'FileC': 1}
        },
        'User2': {
            'files_accessed': {'FileA'},
            'file_access_counts': {'FileA': 1}
        },
        'User3': {
            'files_accessed': {'FileD'},
            'file_access_counts': {'FileD': 1}
        }
    }
    
    assert stats == expected