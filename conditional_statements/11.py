units = int(input("ENTER THE UNITS : "))

if units <= 100:
    print("No charge")
elif(units >=100 and units <=200):
    print(units*5)
else:
    print(units*10)