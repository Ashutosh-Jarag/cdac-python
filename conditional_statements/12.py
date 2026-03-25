percentage = int(input("ENTER THE PERCENTAGE : "))

if percentage >= 90:
    print("grade A")
elif(percentage >=80 and percentage <90):
    print("grade B")
elif(percentage >=70 and percentage <80):
    print("grade C")
elif(percentage >=60 and percentage <70):
    print("grade D")
else:
    print("grade F")