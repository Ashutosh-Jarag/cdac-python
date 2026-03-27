
int

print("-"*40)

#2

dict1 = {1:'a',2:'b',3:'c'}
dict2 = {4:'d', 5:'e'}

merged = {**dict1,**dict2}

print(merged)

print("-"*40)


#3


dict3 = {k: k*k*k for k in range(1,10)}
print(dict3)


print("-"*40)

#4
dict4 = {'a':5,'b':3,'c':9}
result = 1
for i in dict4.values():
    result = result * i 
print(result)
    
print("-"*40)

#5
key = 3

dict5 = {1:'a',2:'b',3:'c'}
pop = dict5.pop(key)
print(pop)

del dict5[1]

print(dict5)

print("-"*40)

#6

dict6 = {"name":"ramu", "age":20,"state":"goa"}
dict6["location"] = dict6.pop("state")
print(dict6)


print("-"*40)

#7 
list1 = [1,2,3]
list2 = ['a','b','c']

list3 = [4,5,6,7,8]
list4 = ['1','2','3']

print(dict(zip(list1,list2)))

print(dict(zip(list3,list4)))


#print(dict(zip(list3,list4, strict = True)))



print("-"*40)


#8

dict8 = {'m':"MATH",'p':"PYTHON",'aj':"ADV JAVA"}

print("1 : DISPLAY ")
print("2 : FIND ")
print("3 : ADD ")
print("4 : UPDATE ")
print("5 : DELETE ")
print("6 : UPDATE KEY")


#choice = int(input("ENTER YOUR CHOICE : "))
choice = 1

match choice: 
    case 1:
        print(dict8)
    
    case 2:
        n = input("ENTER THE KEY TO FIND THE VALUE:")
        print(f"value of key {n} is", dict8.get(n))
        
    case 3:
        k = input("ENTER THE KEY : ")
        v = input("ENTER THE VALUE : ")
        dict8[k] = v
        print("ADDED ! ",dict8) 
        
    case 4:
        k = input("ENTER THE KEY : ")
        v = input("ENTER THE VALUE : ")
        dict8[k] = v
        print("UPDATE ! ",dict8)
        
    case 5:
        k = input("ENTER THE KEY TO DELETE  : ")
        dict8.pop(k)
        print("DELETED! ",dict8)
        
    case 6:
        k = input("ENTER THE KEY TO UPDATE : ")
        newK = input("NEW NAME TO UPDATE : ")
        dict8[newK] = dict8.pop(k)
        print("AFTER THE RENMAE : ", dict8)
        
    
    case '_':
        print("INVALID.")
        
        
        

print("-"*30)

#9 


dict9 = {"madura":"1234567890", "ram": "2345678901", "rama":"3456789012"}
dict9.update({"madura":"0987654321"})
print("1 --",dict9)

dict9["ankita"] = "38423489723"
print("2 --", dict9)

print("3 -- ",dict9["ram"])

dict9.setdefault("sakshi")
print("4 -- ", dict9)

print("Print all keys : ",dict9.keys())

print("Print all values : ",dict9.values())

print("Print all keys : ",list(dict9.keys()))

print("Print all values : ",list(dict9.values()))

for i in dict9.keys():
    print(i)
    
for i in dict9.values():
    print(i)
    
i = 1
for i ,(k,v) in enumerate(dict9.items()):
    print(i,k,v)








