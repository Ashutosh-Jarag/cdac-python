#Return a list containing length of each word.

l1 = ['a',"dfd","fdss","dfsdf"]

print(list(map(lambda x:len(x),l1)))
print(list(map(len, l1)))