import sqlite3

# Quick script to check what's actually in the users table - not part of the
# app itself, just something I run manually to check the database is working
conn = sqlite3.connect("photography_app.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print("Users in database:")
for user in users:
    print(user)
conn.commit()
conn.close()
