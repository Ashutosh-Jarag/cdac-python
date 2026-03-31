class Person:
    def __init__(self, pid=1, pname="dhannu", email="dhannu69@gmail.com", mobno=9922886644):
        self.pid = pid
        self.pname = pname
        self.email = email
        self.mobno = mobno
        
    def display(self):
        print(self.pid)
        print(self.pname)
        print(self.email)
        print(self.mobno)
        
        
class Emp(Person):
    def __init__(self,dept, desg, sal):
        super().__init__()
        self.dept = dept 
        self.desg =desg
        self.sal = sal
        
    def display(self):
        super().display()
        print(self.dept)
        print(self.desg)
        print(self.sal)
    
    def calNetSal(self):
        if self.sal > 2000:
            self.sal = self.sal*1.1
        elif self.sal > 1000 and self.sal < 2000:
            self.sal = self.sal*1.5
        else :
            self.sal = self.sal* 0.5
        print(self.sal)
        
        
p = Person()
p.display()

print("="*30)
            
e = Emp("IT", "Developer", 2500)
e.display()
e.calNetSal()

e1 = Emp(101, "Rahul", "rahul@gmail.com", 9922886644,"IT", "Developer", 2500)
e1.display()
e1.calNetSal()

