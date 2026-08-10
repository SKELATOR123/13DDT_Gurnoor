import sqlite3
conn = sqlite3.connect("photography_app.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print("Users in database:")
for user in users:
    print(user)
conn.commit()
conn.close()