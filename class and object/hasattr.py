class Student:
    def __init__(self, name):
        self.name = name

s = Student("Rahul")

# without hasattr — risky!
#print(s.marks)   # ❌ AttributeError!

# with hasattr — safe!
if hasattr(s, "marks"):
    print(s.marks)
else:
    print("marks not found!")   # ✅ safe!
    
class Student:
    def __init__(self):
        self.name  = "Rahul"
        self.marks = 85

s = Student()

# hasattr → check if exists
hasattr(s, "name")      # True

# getattr → get value safely
getattr(s, "name")      # "Rahul"
getattr(s, "age", 0)    # 0 ← default if not found!

# setattr → set value
setattr(s, "age", 20)   # s.age = 20
print(s.age)            # 20 ✅

# delattr → delete attribute
delattr(s, "marks")     # del s.marks
print(hasattr(s, "marks"))  # False ✅