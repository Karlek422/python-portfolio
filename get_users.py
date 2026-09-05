import mysql.connector

db = mysql.connector.connect(
     host="localhost", 
     user="root",
     password="", 
     database="соц",  # назва твоєї бази з панелі phpMyAdmin 
)
cursor = db.cursor()

cursor.execute("SELECT id, username, emeil FROM users;")
print("Список твоїх користувачів із бази:")
print("-" * 40)
for row in cursor.fetchall():
      print(f"ID: {row[0]} | Ім'я: {row[1]} | Пошта: {row[2]}")
db.close()