class Shape:
    def area(self):
        return 0                    

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):                 
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):                 
        return self.w * self.h

c = Circle(5)
r = Rectangle(4, 5)
print(c.area())    # 78.5
print(r.area())    # 20