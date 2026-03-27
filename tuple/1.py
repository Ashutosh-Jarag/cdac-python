#1

tuple1 = ('a','e','i','o','u')

print("".join((tuple1)))

print("-"*30)  
  
#2

tuple2 = (1,2,3,4,5,6,7,8,9,10,'a','b', 'c')

print(tuple2[3:4]+tuple2[-2:-3:-1])



print("-"*30)    

#3

n = 1
tuple3 = (1,2,3,4,5,6,7,8,1,2,3,1,4,5,1)
count = 0 

for i in tuple3:
    if i == n :
        count+=1
        
print(count)

print(tuple3.count(1))

print("-"*30)    

#4

tuple4 = (1,2,3,4,5,6,7,'a','b')

n1 = 4
n2 = 'b'
if n in tuple4:
    print("It exists at",tuple4.index(n1))
    print(tuple4.index(n2))
    
print("-"*30)    


#5
tuple5 = (1,2,3,4,5,6,7,8,1,2,3,1,4,5,1)      

print(min(tuple5))
print(max(tuple5))

print("-"*30)    

#6

tuple6 = (1,2,3,4,5,6,7,'a','b')

print(tuple6.index(5))
print(tuple6.index('a'))

print("-"*30) 

#7
n = 5
tuple7 = (1,2,3,4,5,6,7,8,1,2,3,1,4,5,1)
count = 0 

for i in tuple7:
    if i == n :
        count+=1
        
print(count)


print("-"*30) 

# 8 
tuple8 = (1,2,3,4,5)
sum = 0

for i in tuple8:
    sum+=i
print(sum)

print("-"*30) 
    
# 9
string = "abcdefjh"
print(tuple(string))

print("-"*30) 

#10

tuple10 = tuple(string)
print(tuple10[::-1])






