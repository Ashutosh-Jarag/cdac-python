class Animal:
    def speak(self):
        print("Animal makes sound!")  

class Dog(Animal):
    def speak(self):                   
        print("Dog says Woof!")

class Cat(Animal):
    def speak(self):                 
        print("Cat says Meow!")
        
        
class Fish(Animal):
    def speak(self):
        super().speak()                        #super method
        print("Fish Fish")

# test
a = Animal()
a.speak()   

d = Dog()
d.speak()    

c = Cat()
c.speak()    

f = Fish()
f.speak()