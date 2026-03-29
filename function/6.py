#Convert a list of strings to uppercase using map().

l1 = ['abc','xyz','pqr']

print(list(map(lambda x:x.upper(),l1)))

print(list(map(str.upper,l1)))