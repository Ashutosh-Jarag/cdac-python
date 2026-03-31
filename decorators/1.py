def greet():
    print("Hello")
    
#greet()

#test=greet
#test()


def greet1():
    print("Hi")

def extra_info():
    print("Before function call: ")
    greet()
    print("After Function call")
    
extra_info()