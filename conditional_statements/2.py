maths = int(input("ENTER THE MARKS OF THE MATHS : "))
chem =  int(input("ENTER THE MARKS OFT THE CHEMISTRY : "))
phy = int(input("ENTER THE MARKS OF THE PHYSICS : "))

total = maths + chem + phy
print("TOTAL MARKS : ", total)
per = total / 3
print("PERCENTAGE : ", per)

if per >= 80:
    print("DISTINCTION")
elif per >= 60:
    print("FIRST CLASS")
elif per >= 50:
    print("SECOND CLASS")
else:
    print("FAIL")