class Student:
    
    # constructor
    def __init__(self, name, age, marks):
        print(f"Student {name} created!")
        self.name  = name      
        self.age   = age       
        self.marks = marks    
    
    # methods
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age:  {self.age}")
        print(f"Marks:{self.marks}")
    
    def isPassed(self):
        if self.marks >= 40:
            return f"{self.name} Passed! ✅"
        return f"{self.name} Failed! ❌"
    
    def grade(self):
        if self.marks >= 90: return "A"
        elif self.marks >= 80: return "B"
        elif self.marks >= 70: return "C"
        elif self.marks >= 40: return "D"
        else: return "F"
    
    # destructor
    def __del__(self):
        print(f"Student {self.name} removed!")


# create objects (instances)
s1 = Student("Rahul", 20, 85)   
s2 = Student("Priya", 21, 35)  

# call methods
s1.display()
print(s1.isPassed())  
print(s1.grade())      

s2.display()
print(s2.isPassed())   
print(s2.grade())      

# delete object
del s1   







### Practice:
"""
1. Create a BankAccount class with
   → balance, deposit(), withdraw()
2. Create a Animal class with
   → name, sound, speak()
3. Create a Rectangle class with
   → width, height, area(), perimeter()
   
"""