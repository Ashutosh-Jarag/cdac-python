"""
From a list of numbers:

First filter even numbers and Then square them

Convert list of string numbers to integers.

"""

l = [1,2,3,4,5]

print(list(map(lambda x: x*2, filter(lambda x: x%2==0, l))))


l = ["1","2","3","4","5"]
print(l)
result = list(map(lambda x: int(x) , l))   
print(result)