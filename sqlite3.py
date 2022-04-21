import sqlite3

#Create, read, update, delete

db = sqlite3.connect('users.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pupils(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR,
	school VARCHAR,
	grade INTEGER
	)""") # Create request
db.commit()

cursor.execute("""INSERT INTO pupils(name, school, grade) VALUES (?, ?, ?)""", ("Витя", "Школа 13123", 5))
db.commit()

#cursor.execute("""DELETE FROM pupils WHERE name=?""", ("Витя",))
#db.commit()

cursor.execute("""SELECT * FROM pupils""")
print(cursor.fetchall())

print("################################################################################################################")

cursor.execute("""UPDATE pupils SET name=? WHERE id=8""", ("Андрей",))
db.commit()

cursor.execute("""SELECT * FROM pupils""")
print(cursor.fetchone())
