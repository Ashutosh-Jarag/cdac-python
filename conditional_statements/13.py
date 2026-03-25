price = int(input("ENTER THE BIKE PRICE : "))

if price > 100000:
    print(price*0.15)
elif(price > 50000 and price <=100000):
    print(price*0.10)
elif(price > 10000 and price <=50000):
    print(price*0.05)
else:
    print(price*0.02)