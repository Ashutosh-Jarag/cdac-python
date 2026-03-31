import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NewPassword123",
    database = "pythondemo"
)

cursor = conn.cursor()


cursor.execute("UPDATE student SET marks = 78.01 WHERE name= 'Rama'")

conn.commit()

print(f"{cursor.rowcount} RECORD UPDATED SUCCESSFULLY")

cursor.execute("SELECT * FROM student")

for row in cursor:
    print(row)

conn.close()


