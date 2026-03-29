students = [
    {"name": "Amit", "marks": 78, "age": 20},
    {"name": "Sneha", "marks": 92, "age": 22},
    {"name": "Rahul", "marks": 65, "age": 19},
    {"name": "Priya", "marks": 88, "age": 21},
    {"name": "John", "marks": 55, "age": 20}
]

employees = [
    {"name": "Raj", "salary": 25000},
    {"name": "Simran", "salary": 40000},
    {"name": "Aman", "salary": 18000},
    {"name": "Neha", "salary": 32000}
]

#Q1. Extract Student Names

print(list(map(lambda x: x['name'],students)))


#Q2. Students with Marks > 75

print(list(map(lambda x : x['name'],filter(lambda x: x['marks']>75,students))))


#Q3. Scholarship Students (≥ 85)

print(list(map(lambda x : f"Scholorship got student name is {x['name']} and marjs is {x['marks']}",
               filter(lambda x: x['marks']>=85,students))))




#Q4. Names of Failed Students
print(list(map(lambda x : x['name'],filter(lambda x: x['marks']<70,students))))

print(list(filter(lambda x: x['marks']<70,students),(map(lambda x : x['name']))))


#Q5. Return names of students:
#	Age > 20 	Marks > 80

print(list(map(lambda x : x['name'],filter(lambda x: x['marks']>80 and x['age']>20,students))))



employees = [
    {"name": "Raj", "salary": 25000},
    {"name": "Simran", "salary": 40000},
    {"name": "Aman", "salary": 18000},
    {"name": "Neha", "salary": 32000}
]


#Q1. High Salary Employees (> 30000)
print(list(map(lambda x : x['name'],filter(lambda x: x['salary']<30000,employees))))


#Q2. Names of Low Salary Employees (< 25000)

print(list(map(lambda x : x['name'],filter(lambda x: x['salary']<25000,employees))))

#Q3. Special Filter:Filter employees: Salary > 20000 and Name starts with 'N'

print(list(map(lambda x : x['name'],
               filter(lambda x: x['salary']>20000 and x['name'].startswith('N'),employees))))

print(list(map(lambda x: x['name'],
     filter(lambda x: x['name'][0:1] == 'N' and  x['salary']>20000 , employees))))


print(list(filter(lambda x: x['name'][0:1] == 'N' and  x['salary']>20000 , employees)))






