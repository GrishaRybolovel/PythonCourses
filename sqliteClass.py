import sqlite3

class botDB:

	def __init__(self, db_file):
		self.db = sqlite3.connect(db_file)
		self.cursor = self.db.cursor()

	def add_pupil(self, name, school, grade):
		self.cursor.execute("""INSERT INTO pupils(name, school, grade) VALUES (?, ?, ?)""", (name, school, grade))
		self.db.commit()

	def delete(self, name, school, grade):
		self.cursor.execute("""DELETE FROM pupils WHERE name=? AND school=? AND grade=?""", (name, school, grade))
		self.db.commit()


	def select_one(self):
		self.cursor.execute("""SELECT * FROM pupils""")
		return(self.cursor.fetchone())

	def select_all(self):
		self.cursor.execute("""SELECT * FROM pupils""")
		return(self.cursor.fetchall())

	def update(self, new_name, id_u):
		cursor.execute("""UPDATE pupils SET name=? WHERE id=8""", (new_name, id_u))

	def close(self):
		self.db.close()

newDB = botDB("users.db")

newDB.add_pupil("Карл", "123", 5)
print(newDB.select_all())
