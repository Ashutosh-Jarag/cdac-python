def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero!"
    return a // b


def isPositive(n):
    if n>=0:
        return f"{n} is a POSITIVE NUMBER"
        
    else :
        return f"{n} is a NEGATIVE NUMBER"
        


def isPrime(n):

    
    if n < 2:
        return f"{n} is not a prime number"        
    
    for i in range(2, n):  
        if n % i == 0:
            return f"{n} is a not a prime number"
            break
    
    return f"{n} is a prime number "

def isEven(n):
    
    if n%2==0:
        return f"{n} is EVEN NUMBER"
    else:
        return f"{n} is NOT EVEN NUMBER"
        
        
        
def isArmStrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    
    for d in digits:
        total += int(d)**power
    return f"{n} is Armstrong!" if total == n else f"{n} is not Armstrong!"



def printlist(n):
    print(n)
    
def reverselist(n):
    print(n[::-1])
    
def displayupper(n):
    return n.upper() 

def displaylower(n):
    return n.lower()

def displayUnique(n):
    return list(set(n))

def displayAlterante(n):
    return n[::2]
      
def displayDuplicates(n):
    return [x for x in n if n.count(x) >1]




    
        