# Password Strength Checker

A simple Python-based tool to assess the strength of a password based on complexity criteria such as length, uppercase/lowercase letters, numbers, and special characters. Built for Kali Linux but works on any system with Python 3.

---

## How It Works

The tool evaluates the strength of a password based on the following criteria:

1. **Length**: The password must be at least 8 characters long.
2. **Uppercase Letters**: The password must contain at least one uppercase letter (A-Z).
3. **Lowercase Letters**: The password must contain at least one lowercase letter (a-z).
4. **Digits**: The password must contain at least one digit (0-9).
5. **Special Characters**: The password must contain at least one special character (e.g., `!@#$%^&*()`).

The tool calculates a **strength score** based on how many of these criteria are met and provides feedback on the password's strength:

- **Very Weak**: Meets 0-1 criteria.
- **Weak**: Meets 2 criteria.
- **Moderate**: Meets 3 criteria.
- **Strong**: Meets 4 criteria.
- **Very Strong**: Meets all 5 criteria.

---

## How to Use

### Prerequisites
- Python 3.x (pre-installed on Kali Linux).

### Steps to Run the Tool

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
