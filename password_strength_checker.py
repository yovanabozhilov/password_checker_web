import re
import secrets
import string
from pathlib import Path

class PasswordStrengthChecker:
    def __init__(self, weak_passwords_file='weak_passwords.txt'):
        self.weak_passwords = set()
        self.weak_passwords_file = Path(weak_passwords_file)
        self.load_weak_passwords()

    def load_weak_passwords(self):
        if not self.weak_passwords_file.exists():
            raise FileNotFoundError(f"Cannot find {self.weak_passwords_file}")
        with self.weak_passwords_file.open('r') as f:
            passwords = []

            for line in f:
                cleaned = line.strip()  
                if cleaned:             
                        passwords.append(cleaned)

            self.weak_passwords = set(passwords)

    def check_password_strength(self, password: str) -> str:
        if password in self.weak_passwords:
            return "Weak: This password is commonly used and insecure."
        if len(password) < 8:
            return "Weak: Password must be at least 8 characters."
        if not all([
            re.search(r'[A-Z]', password),
            re.search(r'[a-z]', password),
            re.search(r'\d', password),
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
        ]):
            return "Weak: Password must contain an uppercase letter, lowercase letter, number, and special character."
        if len(password) > 12:
            return "Strong: Password is strong and meets the criteria."
        return "Medium: Password is of medium strength."
    
    def generate_secure_password(self, length=16) -> str:
        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        alphabet = string.ascii_letters + string.digits + string.punctuation

        while True:
            password = ''.join(secrets.choice(alphabet) for _ in range(length))

            if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password)):
                return password
