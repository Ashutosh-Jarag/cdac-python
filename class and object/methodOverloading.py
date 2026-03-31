class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):    
        return a + b + c

calc = Calculator()
#calc.add(1, 2)        # ❌ TypeError! second add replaced first!
print(calc.add(1, 2, 3))     # 6 ✅

print("*"*30)

class Calculator:
    def add(self, a, b, c=0):   
        return a + b + c

calc = Calculator()
print(calc.add(1, 2))      # 3  ✅
print(calc.add(1, 2, 3))   # 6  ✅

print("*"*30)
class Calculator:
    def add(self, *args):         
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))         # 3  ✅
print(calc.add(1, 2, 3))      # 6  ✅
print(calc.add(1, 2, 3, 4))   # 10 ✅

print("*"*30)

class Display:
    def show(self, data):
        if isinstance(data, int):
            print(f"Integer: {data}")
        elif isinstance(data, str):
            print(f"String: {data}")
        elif isinstance(data, list):
            print(f"List: {data}")

d = Display()
d.show(42)           # Integer: 42
d.show("hello")      # String: hello
d.show([1,2,3])      # List: [1,2,3]


### Practice:
"""
1. Create Vehicle → Car → ElectricCar
   override drive() each level

2. Create Calculator with add()
   that handles 2,3,4 numbers using *args

3. Create Shape → Circle, Rectangle, Triangle
   override area() for each
"""