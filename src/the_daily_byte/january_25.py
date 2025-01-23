import re


"""
This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""
def reverse_string(s: str) -> str:
    return s[::-1]

"""
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""
def is_palindrome(s: str) -> bool:
    # Complexity of O(n)
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Compare the string with its reverse
    return cleaned_string == cleaned_string[::-1]

"""
This question is asked by Amazon. 
Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. 
The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""
def returns_to_origin(moves: str) -> bool:
    # Initialize counters for horizontal and vertical movements
    horizontal = 0
    vertical = 0

    # Iterate through each move in the sequence
    for move in moves:
        if move == 'L':
            horizontal -= 1
        elif move == 'R':
            horizontal += 1
        elif move == 'U':
            vertical += 1
        elif move == 'D':
            vertical -= 1

    # The robot returns to the origin if both counters are zero
    return horizontal == 0 and vertical == 0

"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""
def is_capitalized_correctly(s: str) -> bool:
    # Check if all letters are capitalized
    if s == s.upper():
        return True
    # Check if no letters are capitalized
    if s == s.lower():
        return True
    # Check if only the first letter is capitalized
    if s == s.capitalize():
        return True
    # If none of the above, return False
    return False