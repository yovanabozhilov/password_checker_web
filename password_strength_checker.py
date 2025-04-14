import re
import json
import random
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
            self.weak_passwords = set(line.strip() for line in f if line.strip())

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
