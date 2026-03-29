
def stringCount(s):
    count = 0
    for i in s:
        if i.isalpha():
            count+=1
            
    return count


print(stringCount("i v o"))

#using lambda +filer
stringCount = lambda s: len(list(filter(str.isalpha, s)))
print(stringCount("i vdfsdfs o"))

#using filter + lambda
stringCount = lambda s: len(list(filter(lambda x: x.isalpha(), s)))
print(stringCount("i v o"))

#using map()+sum()
stringCount = lambda s: sum(list(map(lambda x: 1 if x.isalpha() else 0, s)))
print(stringCount("i v o"))