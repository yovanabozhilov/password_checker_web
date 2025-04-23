# Password Strength Checker – Flask Web + API

This is a **Flask-based full-stack web application** for registering users with **strong, secure passwords**, backed by custom validation, secure password hashing, and a lightweight JSON-based storage system.

It supports both:

- A **user-friendly web interface** for form registration and viewing users
- A **RESTful API** for programmatic access and Postman testing

---

## Features

### Password Strength Validation
- Minimum 8 characters
- Must include **uppercase**, **lowercase**, **digit**, and **special character**
- Rejects common/weak passwords from `weak_passwords.txt`

### User Registration (Web + API)
- Username
- Email
- Password (with confirmation)
- Uses `bcrypt` to securely hash passwords
- Prevents duplicate usernames and emails

### JSON File Storage
- Users are stored in `users.json` for simplicity
- Uses `json.load()` and `json.dump()` to **parse** and **serialize** JSON

### Password Generator (AJAX)
- Secure password generation using Python’s `secrets` module
- Fills password and confirm fields automatically via JavaScript `fetch()` call to the API

### REST API Endpoints (for Postman or frontend)
- `GET /api/generate-password` → Generate secure password
- `POST /api/register` → Register user via JSON
- `GET /api/users` → View registered users (JSON)

### Web Pages
- `/register` → Web registration form (with password generator)
- `/users` → View list of registered users (HTML)

---

## Tech Stack

- **Python 3.12.7**
- **Flask**
- **HTML/CSS + JavaScript (AJAX)**
- **bcrypt**
- **JSON (for local data storage)**

---

## Setup Instructions

### 1. Clone or download the project

```bash
git clone https://github.com/yovanabozhilov/password_checker_web.git
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

---

## Example API Usage (Postman)

### Register user (POST /api/register)
```json
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "Str0ng!Pass1",
  "confirm_password": "Str0ng!Pass1"
}
```
### Generate password (GET /api/generate-password)
```json
{
  "password": "G7!x@z1LmQ"
}
```
