import re

def check_password_strength(password):
    # Initialize strength score
    strength_score = 0
    feedback = []

    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Evaluate strength based on criteria
    if length_criteria:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if number_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level
    if strength_score == 5:
        strength_level = "Very Strong"
    elif strength_score == 4:
        strength_level = "Strong"
    elif strength_score == 3:
        strength_level = "Moderate"
    elif strength_score == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    # Provide feedback
    if feedback:
        feedback_message = "Feedback: " + " ".join(feedback)
    else:
        feedback_message = "Password meets all complexity requirements."

    return {
        "strength_level": strength_level,
        "feedback": feedback_message
    }

# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result['strength_level']}")
    print(result['feedback'])
