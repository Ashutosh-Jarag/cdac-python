n = int(input("ENTER THE NUMEBR : "))

factorial = 1
i = 1


while i<=n:
    factorial = factorial * i
    i = i+1
    print(i,"! = ", factorial)
    
    
print(factorial)
    