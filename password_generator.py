# password_generator.py
# Author: Your Name
# Date: October 2025
# Description: A simple Python script to generate strong random passwords.
# Great beginner-friendly Hacktoberfest contribution! 🎃

import random
import string

def generate_password(length=12):
    """
    Generates a random secure password of a given length.
    Includes uppercase, lowercase, digits, and symbols.
    """
    if length < 6:
        return "⚠️ Password length should be at least 6 characters."

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        print(f"Generated Password: {generate_password(length)}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
