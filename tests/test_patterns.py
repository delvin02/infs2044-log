import pytest
from output_formatter import generate_output
from patterns import load_patterns
from io import StringIO

def test_load_patterns(monkeypatch):
    # Mock the content of the patterns.csv file, ensuring newlines are correctly handled
    pattern_content = "FileA==0,File A was not accessed\nFileA>0,File A was accessed\nFileD>0,File D was accessed\n"
    
    # Mock the open function to simulate reading from a file
    monkeypatch.setattr('builtins.open', lambda f, mode: StringIO(pattern_content))
    
    # Load the patterns
    patterns = load_patterns("patterns.csv")
    
    # Print loaded patterns for debugging
    print("Loaded patterns:", patterns)
    
    # Verify the loaded patterns
    expected = [
        {'condition': 'FileA==0', 'description': 'File A was not accessed'},
        {'condition': 'FileA>0', 'description': 'File A was accessed'},
        {'condition': 'FileD>0', 'description': 'File D was accessed'}
    ]
    
    # Sort both patterns and expected results by 'condition'
    patterns_sorted = sorted(patterns, key=lambda x: x['condition'])
    expected_sorted = sorted(expected, key=lambda x: x['condition'])

    assert patterns_sorted == expected_sorted

def test_generate_output_basic(capsys):
    # Sample matches
    matches = [
        {'user_id': 'User1', 'message': 'File A was accessed'},
        {'user_id': 'User1', 'message': 'All three files were accessed'},
        {'user_id': 'User2', 'message': 'File A was accessed'},
        {'user_id': 'User3', 'message': 'File D was accessed'}
    ]
    
    # Generate basic output
    generate_output(matches, 'basic')
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Verify the output
    expected_output = "User1,File A was accessed\nUser1,All three files were accessed\nUser2,File A was accessed\nUser3,File D was accessed\n"
    assert captured.out == expected_output

def test_generate_output_grouped(capsys):
    # Sample matches
    matches = [
        {'user_id': 'User1', 'message': 'File A was accessed'},
        {'user_id': 'User1', 'message': 'All three files were accessed'},
        {'user_id': 'User2', 'message': 'File A was accessed'},
        {'user_id': 'User3', 'message': 'File D was accessed'}
    ]
    
    # Generate grouped output
    generate_output(matches, 'grouped')
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Verify the output
    expected_output = "User1:\n    File A was accessed\n    All three files were accessed\n\nUser2:\n    File A was accessed\n\nUser3:\n    File D was accessed\n\n"
    assert captured.out == expected_output
