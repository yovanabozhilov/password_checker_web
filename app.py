from flask import Flask, render_template, request, redirect, url_for, flash
import json
from pathlib import Path
from password_strength_checker import PasswordStrengthChecker

app = Flask(__name__)
app.secret_key = 'super-secret-key'
checker = PasswordStrengthChecker()
users_file = Path('users.json')


def load_users():
    if users_file.exists():
        try:
            with open(users_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_users(users):
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=4)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not username or not email or not password or not confirm_password:
            flash("All fields are required.", "error")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for('register'))

        strength = checker.check_password_strength(password)
        if strength.startswith("Weak"):
            flash(strength, "error")
            return redirect(url_for('register'))

        users = load_users()

        if any(user['username'].lower() == username.lower() for user in users):
            flash(f"Username '{username}' is already taken. Please choose another.", "error")
            return redirect(url_for('register'))

        users.append({
            "username": username,
            "email": email,
            "password": password,
            "strength": strength
        })
        save_users(users)
        flash(f"User '{username}' registered successfully! {strength}", "success")
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/users')
def users():
    users = load_users()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
