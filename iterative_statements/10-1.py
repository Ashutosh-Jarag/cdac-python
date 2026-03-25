n = 5


for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end= ' ')
    print()
    
print("-----------------------------------------------")
    
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end= ' ')
    print()    

print("-----------------------------------------------")


for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=' ')
    print()
    
print("-----------------------------------------------")

for i in range(1,n+1):                     
    for j in range(0,n-i):
        print(" ", end ='')                    
    for k in range(1,i+1):
        print("*", end = '')
    print()
    
    
print("-----------------------------------------------")

for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end='')
    for k in range(0,2*i-1):
        print("*", end='')
    print()


print("-----------------------------------------------")

num = 1
for i in range(1,n+1):
    for j in range(0,i):
        print(num,end='')
        num = num +1
    print()





















