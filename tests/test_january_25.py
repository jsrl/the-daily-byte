from src.the_daily_byte.january_25 import reverse_string, is_palindrome, returns_to_origin, is_capitalized_correctly


# Tests for reverse_string
def test_reverse_string():
    assert reverse_string("Cat") == "taC"
    assert reverse_string("The Daily Byte") == "etyB yliaD ehT"
    assert reverse_string("civic") == "civic"
    assert reverse_string("") == ""  # Edge case: empty string

# Tests for is_palindrome
def test_is_palindrome():
    assert is_palindrome("level") == True
    assert is_palindrome("algorithm") == False
    assert is_palindrome("A man, a plan, a canal: Panama.") == True
    assert is_palindrome("") == True  # Edge case: empty string
    assert is_palindrome("12321") == True  # Numbers as palindrome
    assert is_palindrome("No 'x' in Nixon") == True  # With special characters

# Tests for returns_to_origin
def test_returns_to_origin():
    assert returns_to_origin("LR") == True
    assert returns_to_origin("URURD") == False
    assert returns_to_origin("RUULLDRD") == True
    assert returns_to_origin("") == True  # Edge case: no moves
    assert returns_to_origin("UDLR") == True  # Moves that cancel out

# Tests for is_capitalized_correctly
def test_is_capitalized_correctly():
    assert is_capitalized_correctly("USA") == True
    assert is_capitalized_correctly("Calvin") == True
    assert is_capitalized_correctly("compUter") == False
    assert is_capitalized_correctly("coding") == True
    assert is_capitalized_correctly("") == True  # Edge case: empty string
    assert is_capitalized_correctly("Python") == True  # Only the first letter capitalized
    assert is_capitalized_correctly("PYTHON") == True  # All letters uppercase
    assert is_capitalized_correctly("python") == True  # All letters lowercase