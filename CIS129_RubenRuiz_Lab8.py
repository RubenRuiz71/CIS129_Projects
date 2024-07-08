def is_palindrome(s):

    # Normalize the string: convert to lowercase and remove spaces and punctuation
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Use a stack (implemented as a list) to store characters
    stack = []
    for char in normalized_str:
        stack.append(char)
    
    # Compare characters from the beginning with popped characters from the stack
    for char in normalized_str:
        if char != stack.pop():
            return False
    
    # If all characters match, it's a palindrome
    return True

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
print(is_palindrome("radar"))  # True
print(is_palindrome("hanah"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome(""))  # True (empty string is considered a palindrome)
