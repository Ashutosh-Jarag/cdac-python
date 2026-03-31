class Student:
    def __init__(self, name, rollno):
        self.name= name
        self.rollno = rollno
        
    def display(self):
        print(self.name, self.rollno)

        
    def setAge(self, age):
        self.age = age
        print(self.age)
        
    def setMarks(self, marks):
        self.marks = marks
        print(self.marks)
        
    
s1 = Student("raj", 12)
s1.display()
s1.setAge(20)
s1.setMarks(90)
s1.display()