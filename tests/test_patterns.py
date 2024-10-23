import pytest
from output_formatter import OutputGenerator
from patterns import PatternMatcher
from io import StringIO

def test_load_patterns(monkeypatch):
    # Mock the content of the patterns.csv file, ensuring newlines are correctly handled
    pattern_content = "FileA==0,File A was not accessed\nFileA>0,File A was accessed\nFileD>0,File D was accessed\n"
    
    # Mock the open function to simulate reading from a file
    monkeypatch.setattr('builtins.open', lambda f, mode: StringIO(pattern_content))
    
    # Load the patterns
    pattern_matcher = PatternMatcher("patterns.csv")
    patterns = pattern_matcher.load_patterns()
    
    # Print loaded patterns for debugging
    print("Loaded patterns:", patterns)
    
    # Verify the loaded patterns
    expected = [
        {'condition': 'FileA==0', 'description': 'File A was not accessed'},
        {'condition': 'FileA>0', 'description': 'File A was accessed'},
        {'condition': 'FileD>0', 'description': 'File D was accessed'}
    ]
    

    assert patterns == expected