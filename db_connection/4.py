import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NewPassword123",
    database = "pythondemo"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

for row in cursor:
    print(row)

conn.close()