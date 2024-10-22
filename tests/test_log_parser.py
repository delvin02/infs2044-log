from io import StringIO
from log_parser import parse_log_file

def test_parse_log_file(monkeypatch):
    # Mock the content of the log.csv file
    log_content = """User1,FileA
User2,FileA
User1,FileB
User1,FileA
User3,FileD
User1,FileC"""
    
    # Mock the open function to simulate reading from a file
    monkeypatch.setattr('builtins.open', lambda f, mode: StringIO(log_content))
    
    # Parse the log file
    log_entries = parse_log_file("log.csv")
    
    # Verify the parsed log entries
    expected = [
        {'user_id': 'User1', 'file_accessed': 'FileA'},
        {'user_id': 'User2', 'file_accessed': 'FileA'},
        {'user_id': 'User1', 'file_accessed': 'FileB'},
        {'user_id': 'User1', 'file_accessed': 'FileA'},
        {'user_id': 'User3', 'file_accessed': 'FileD'},
        {'user_id': 'User1', 'file_accessed': 'FileC'},
    ]
    
    assert log_entries == expected