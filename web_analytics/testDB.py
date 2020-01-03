import MySQLdb


Con = MySQLdb.Connect(host="34.82.204.253", port=3306, user="nimbus", passwd="HeyN1mbus!", db="dev")
Cursor = Con.cursor()
sql = "SELECT * FROM Courses"
Cursor.execute(sql)
names = [row[5] for row in Cursor.fetchall()]
print(names)
