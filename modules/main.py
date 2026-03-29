from mModule import *  

print(add(10, 10))   
print(sub(10, 5))
print(mul(10, 5))
print(div(10, 5))


print(isPrime(7))
print(isPrime(4))

print(isEven(10))
print(isEven(7))


print(isPositive(5))
print(isPositive(-1))

print(isArmStrong(153))
print(isArmStrong(135))


l1 = [1,2,3,4,5]
printlist(l1)
reverselist(l1)

l2 = ["Hello", "Hi", "Bye"]
print(list(map(displayupper, l2)))

l = [1,2,2,3,3,3,4,5,6]

print("Alternate  :", displayAlterante(l))

print("Unique     :", displayUnique(l))

print("Duplicates :", displayDuplicates(l))






