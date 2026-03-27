
#1
def details(name, age):
    return f"Your name is {name} and age is {age}"
  
print(details("rahul",20))


print("-"*40)



#2
def add(a,b):
    return a+b,a-b


print(add(10,5))

print("-"*40)


#3
def sq(n):
    return n*n

square = sq
print(square(2))


print("-"*40)


#4
def list1(a,b):
    return {x for x in range(a,b) if x%2 == 0}

print(list1(4,30))


print("-"*40)


#5
def ulst(list1):
    list1 = set(list1)
    return list1

list1 = [1,1,1,2,3,4,3,4]
print(ulst(list1))
