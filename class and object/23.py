class Person:
    def __init__(self, pid=1, pname="Mannu", email="imannu12@gmail.com", mobno=12):
        self.pid = pid
        self.pname = pname
        self.email = email
        self.mobno = mobno
        
    def display(self):
        print(self.pid,self.pname,self.email,self.mobno)


class member(Person):
    def __init__(self, mType, AmtPaid):
        self.mType = mType
        self.AmtPaid = AmtPaid
        
    def display(self):
        super().__init__()
        print(self.mType, self.AmtPaid)
    
p = Person()
p.display()

m = member("ROyaL",50)
m.display()