import sqlite3
import hashlib

DB_NAME = "photography_app.db"

# Set up the database and create the users table if it doesn't already exist.
# This runs once, the first time this file gets imported.
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

conn.commit()


def hash_password(password):
    """Turns a password into a scrambled hash so the real password is never stored."""
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    """Adds a new user to the database. Returns (True, message) or (False, message)."""
    if not username or not password:
        return False, "Fields cannot be empty."
    hashed = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        return True, "Registration successful!"
    except sqlite3.IntegrityError:
        # This happens if the username is already taken (UNIQUE in the table above)
        return False, "Username already taken."
    finally:
        conn.close()


def login_user(username, password):
    """Checks if the username/password match a user in the database. Returns True/False."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed = hash_password(password)

    # Hash the entered password and compare it to the hash already stored,
    # rather than storing/comparing real passwords
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed))
    user = cursor.fetchone()
    conn.close()

    return user is not None
