import pickle


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name)
        print(self.age)
        
        


p = Person("backchoda", 20)

with open("file3.pkl","wb") as f:
    pickle.dump(p,f)
    
    
print("Picked Successfully...")


with open("file3.pkl","rb") as f:
    result = pickle.load(f)
    
print(result.name, result.age)