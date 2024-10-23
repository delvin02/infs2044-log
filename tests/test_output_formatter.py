
import pytest
from output_formatter import generate_output

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
    expected_output = "User1:\n    File A was accessed\n    All three files were accessed\nUser2:\n    File A was accessed\nUser3:\n    File D was accessed\n"
    assert captured.out == expected_output
