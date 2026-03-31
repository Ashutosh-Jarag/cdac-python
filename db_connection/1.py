import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NewPassword123",
    database = "pythondemo"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student(rollno INT PRIMARY KEY, name VARCHAR(50), marks DECIMAL(10,2))")

print("TABLE CREATED SUCCESSFULLY")

conn.close()


