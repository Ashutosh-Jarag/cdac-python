def genrate_square(n):
    for i in range(1,n):
        yield i*5
        
        
gen = genrate_square(10)
print(next(gen))   
print(next(gen))
print(next(gen))