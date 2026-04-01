class user:
    def __init__(self,name,age,h,w):
        self.name= name
        self.age = age
        self.h= h 
        self.w= w 

    def display(self):
        try:
            if not isinstance (self.name, str):
                raise TypeError("Name must be a string")
            if not isinstance (self.age, int):
                raise TypeError("Age must be an integer")
            if not isinstance (self.h, int):
                raise TypeError("Height must be an integer")
            if not isinstance (self.w, int):
                raise TypeError("Weight must be an integer")
        except TypeError as e:
            print(e)
        
        else:
            print("All types are valid")
            print("Name : ", self.name)
            print("Age ", self.age)
            print("Height : ", self.h)
            print("Weight : ", self.w)



u = user("abhi", 20, 170, 60)

u.display()

# u1 = user("abhi", "22", 170, 60)
# u1.display()
