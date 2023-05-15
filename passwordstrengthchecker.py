import re

def check_password_strength(password):
    """Check the strength of a password and return a score between 0 and 10."""
    
    # Define a list of regex patterns to check for various password criteria
    patterns = [
        r'[a-z]', # lowercase letters
        r'[A-Z]', # uppercase letters
        r'\d', # digits
        r'[!@#$%^&*()_+}{":?><,./;\'\[\]]' # special characters
    ]
    
    # Check if the password meets each pattern and assign a score between 0 and 2 for each
    score = 0
    for pattern in patterns:
        if re.search(pattern, password):
            score += 2
    
    # Check the length of the password and assign a score between 0 and 2
    if len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    
    # Return the final score between 0 and 10
    return score

# Example usage
password = input("Enter a password to check its strength: ")
score = check_password_strength(password)
print("The strength of your password is:", score, "/ 10")
