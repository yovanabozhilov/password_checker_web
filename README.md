# Password Strength Checker

This is a Flask-based web application for registering users with secure passwords. It includes custom password strength validation, JSON-based data storage, and a simple UI for managing registered users.

---

## Features

Password strength validation:
- At least 8 characters  
- Must include uppercase, lowercase, digits, and special characters  
- Rejects weak/common passwords (loaded from `weak_passwords.txt`)

User registration form with:
- Username
- Email
- Password
- Confirm Password

JSON-based user storage (`users.json`)

User management page to:
- View registered users

---

## Running the App

### 1. Clone or download the project

```bash
git clone https://github.com/your-username/password_checker_web.git
cd password_checker_web
```
Or simply extract the ZIP into a folder and navigate into it.

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```
You should see output like:

```csharp
 * Running on http://127.0.0.1:5000
```
Open your browser and visit:
http://127.0.0.1:5000
