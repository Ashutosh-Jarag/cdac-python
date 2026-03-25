a = int(input("ENTER THE NUMBER : "))
b = int(input("ENTER THE NUMBER : "))
c = int(input("ENTER THE NUMBER : "))

if a > b and a > c:
    print("LARGEST NUMBER IS : ", a)
elif b > a and b > c:
    print("LARGEST NUMBER IS : ", b)
else:
    print("LARGEST NUMBER IS : ", c)