class Shape:
    def  area(self):
        return "guguigui"                    

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):                 
        return 3.14 * self.r ** 2
    
    
class Square(Shape):
    def __init__(self,s):
        self.s = s
        
    def area(self):
        return self.s*self.s

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def area(self):                 
        return self.w * self.h

c = Circle(5)
s = Square(4)
r = Rectangle(4, 5)

print(c.area())    
print(r.area())    
print(s.area())

print("="*30)

for shape in [Circle(10), Square(10), Rectangle(5,5)]:
    print(shape.area())
