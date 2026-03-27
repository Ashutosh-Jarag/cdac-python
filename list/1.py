#1
list1 = [1,2,3,4,5,6,7,8,9]

avg = sum(list1)/len(list1)

print(avg)


total = 0
for i in list1:
    total +=i
avg = total/len(list1)

print(avg)

print("-"*30)

#2
list2 = [-2,-1,0,1,2,3,4,5]
negative = 0 
peven = 0
podd = 0
zero = 0

for i in list2:
    if i < 0:
        negative +=1
    elif i>0:
        if i%2==0:
            peven +=1
        else :
            podd +=1
    else: 
        zero+=1
            
print(negative)
print(peven)
print(podd)
print(zero)

print("-"*30)

#3

even= 0
odd = 0
demoeven = []
demoodd = []

list3 = [-2,-1,0,1,2,3,4,5]
for i in list3:
    if i%2 == 0:
        demoeven.append(int(i))
    elif i%2!=0:
        demoodd.append(int(i))
        
print(max(demoeven))
print(max(demoodd))


print("-"*30)

#4 
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THUSDAY','FRIDAY','SATURDAY','SUNDAY']

list4 = [i[0:3] for i in days]

print(list4)

print("-"*30)

#5
list5 = [1,2,3,4,5,6,7,1,2,4,5,2,1,2]

print(list5.count(2))

#n= int(input("ENter : "))
#s = list5.count(n)
#print(s)

print("-"*30)
#6
list6 = [1,2,3,4,5,6,67,7,8,8]

print(max(list6))

print("-"*30)
#7


list7 = [1,2,3,4,5,6,67,7,8,8]

print("largest = ", max(list7))
sorted_list = list7.sort()
print("second largest = ", list7[-2])

sorted_list = sorted(list7)
print(sorted_list[-2])

set1 = sorted(set(list7))
print(set1[-2])
       
list7 = [1,2,3,4,5,6,67,67,7,8,8]
largest = list7[0]
for i in list7:
    if i > largest:
        largest = i
        
second = 0
for i in list7:
    if i > second and i != largest:
        second = i
print(largest)
print(second)        


print("-"*30)
#8
evenlist = []
oddlist = []
    
list8 = [1,2,3,4,5,6,67,67,7,8,8]

for i in list8:
    if i%2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
        
print(evenlist)
print(oddlist)

print("-"*30)


#9
list9a= [1,2]
list9b = [3,4]

print(sorted(list9a+list9b))

print("-"*30)
    
    
#10
list10 = [1,2,3,4,5]

list10[0],list10[-1] = list10[-1],list10[0]

print(list10)

print("-"*30)

#11
list11 = [1,2,3,4,5,6,67,67,7,8,8]

print(set(list11))

print