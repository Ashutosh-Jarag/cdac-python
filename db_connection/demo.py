import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NewPassword123",
    database = "knowit"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student where rollno in (1,2,3,4,5)")

for row in cursor:
    print(row)

conn.close()

# import mysql.connector
# import tabulate as tb

# conn = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "NewPassword123",
#     database = "knowit"
# )

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM student where per > 90 order by per desc")

# print(tb.tabulate(cursor,headers=["rollno","firstname","lastname","dob","percentage"],tablefmt="psql"))

# conn.close()