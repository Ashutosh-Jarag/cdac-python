class rectangle:
    def __init__(self,l,b):
        self.l = l 
        self.b = b
        
    def area(self):
        return self.l*self.b
    
    def perimeter(self):
        return 2*(self.l+self.b)
    
    
r = rectangle(10, 10)
print(r.area())
print(r.perimeter())
    
    