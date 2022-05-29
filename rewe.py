import sqlite3
db = sqlite3.connect('server.db')
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS users (
    userid INT PRIMARY KEY,
	fname TEXT,
	lname TEXT,
	gander TEXT);

	""")

db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    userid INT PRIMARY KEY,
	date TEXT,
	userid TEXT,
	total TEXT);

	""")

db.commit()

sql.execute("""INSERT INTO users(userid, fname, lname, gander) 
    VALUES ('00001', 'Sasha', 'Ivanova', 'Female');""") 
db.commit()

users = ('00002', 'Marta', 'Lane', 'Female')

sql.execute('''SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN users ON users.userid=orders.userid;''')
print(sql.fetchall())

db.comit()


