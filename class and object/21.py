class Person:
    def __init__(self, pid=1, pname="dfsd", email="fdsf", mobno=12):
        self.pid = pid
        self.pname = pname
        self.email = email
        self.mobno = mobno
        
    def display(self):
        print(self.pid)
        print(self.pname)
        print(self.email)
        print(self.mobno)
        
    
p = Person()
p.display()