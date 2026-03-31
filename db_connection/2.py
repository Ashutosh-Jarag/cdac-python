import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NewPassword123",
    database = "pythondemo"
)

cursor = conn.cursor()

stud = [
    (10, "Ruturaj", 45.97),
    (11, "Rama", 67.80),
    (13,"Vidula",87.20),
    (12,"Ritika",81.34),
    (20,"Kartik",35.00)
]


cursor.executemany("INSERT INTO student VALUES(%s,%s,%s)",stud)


conn.commit()

print(f"{cursor.rowcount} RECORDS INSERTED SUCCESSFULLY")

# cursor.execute("SELECT * FROM student")

# for row in cursor:
#     print(row)



conn.close()


