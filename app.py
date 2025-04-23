from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
from pathlib import Path
from password_strength_checker import PasswordStrengthChecker
import bcrypt

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

@app.route('/register', methods=['GET', 'POST'])
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
            flash("Username already exists.", "error")
            return redirect(url_for('register'))

        if any(user['email'].lower() == email.lower() for user in users):
            flash("Email already exists.", "error")
            return redirect(url_for('register'))

        users.append({
            "username": username,
            "email": email,
            "password": bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            "strength": strength
        })

        save_users(users)
        flash(f"User '{username}' registered successfully! {strength}", "success")
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()

    username = str(data.get('username', '')).strip()
    email = str(data.get('email', '')).strip()
    password = str(data.get('password', '')).strip()
    confirm_password = str(data.get('confirm_password', '')).strip()

    if not username or not email or not password or not confirm_password:
        return jsonify(error="All fields are required."), 400

    if password != confirm_password:
        return jsonify(error="Passwords do not match."), 400

    strength = checker.check_password_strength(password)
    if strength.startswith("Weak"):
        return jsonify(error=strength), 400

    users = load_users()

    if any(user['username'].lower() == username.lower() for user in users):
        return jsonify(error="Username already exists."), 400

    if any(user['email'].lower() == email.lower() for user in users):
        return jsonify(error="Email already exists."), 400

    users.append({
        "username": username,
        "email": email,
        "password": bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        "strength": strength
    })

    save_users(users)
    return jsonify(message="User registered successfully", strength=strength), 201


@app.route('/users')
def users():
    users = load_users()
    return render_template('users.html', users=users)


@app.route('/api/generate-password', methods=['GET'])
def api_generate_password():
    try:
        length = int(request.args.get('length', 16))
        password = checker.generate_secure_password(length=length)
        return jsonify(password=password), 200
    except ValueError as e:
        return jsonify(error=str(e)), 400



if __name__ == '__main__':
    app.run(debug=True)
