def even_numbers(n):
    for i in range(0,n):
        if i%2 == 0:
            yield i
            
            
gen = even_numbers(10)
print(next(gen))   
print(next(gen))
print(next(gen))