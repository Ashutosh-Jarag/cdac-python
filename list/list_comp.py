

result = [x%2 == 0 for x in range(1,20)]
print(result)

print("*"*40)

result = [x for x in range(1,20) if x%2 == 0]
print(result)

print("*"*40)

result = [x*x for x in range(1,11)]
print(result)

print("*"*40)

list1 = ["hello", "world", "pyhton"]
result = [x.upper() for x in list1]
print(result) 

print("*"*40)

list2=["cat", "elephant", "dog", "butterfly"]
result = [len(x) for x in list2]
print(result)

print("*"*40)


list5 = [-1,-3, 1,3,4]
result = [x for x in list5 if x>0]
print(result)

