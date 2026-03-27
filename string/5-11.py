s = "Hello Ashutosh"

c = "Hello maritn your gmail is martin123@gmail.com"

print(s.replace('A', '$'))

print("-"*30)

print(s.replace(s[4], ' '))


print("-"*30)

vowels = 'aeiouAEIOU'
count = 0
for i in s:
    if i.isalpha():
        if  i in vowels:
            count +=1
print(count)

print("-"*30)

print(s.replace(' ', '-'))

print("-"*30)


lenght=0
for i in s:
    if i.isalpha():
        lenght+=1

print(lenght)

print("-"*30)


print((s[::2]))

print("-"*30)



l = 0
u = 0
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print(u)
print(l)


print("-"*30)


vowels = 'aeiouAEIOU'
count = 0
for i in s:
    if i.isalpha():
        if  i not in vowels:
            count +=1
print(count)

print("-"*30)


string  = "Hello, I am 1st in class but my friends are 2nd and 3rd"
list = []

for i in string:
    if i.isdigit():
        list.append(int(i))
sum = 0        
for i in list:
    sum +=i
    
print(sum)


sum = 0 
for i in string:
    if i.isdigit():
        sum+=int(i)
print(sum)

print("-"*30)       


string = "abc12-rt9"
count = 0
for i in string:
    if i.isalpha():
        count+=1
print(count)
        







            