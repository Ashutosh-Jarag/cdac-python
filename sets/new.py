

#demo 
s = {1, 2, 3, 4, 5}

s1 = {1, 2, 3}                    # direct
s2 = set([1, 2, 2, 3, 3])         # from list → {1,2,3} removes duplicates!
s3 = set()                         # empty set
s1.add(4)              # add single element
s1.update([5,6,7])     # add multiple elements
s1.remove(3)           # remove → KeyError if not found!
s1.discard(3)          # remove → NO error if not found ✅
s1.pop()               # removes random element
s1.clear()             # removes all elements

s1 = {1,2,3,4}
s2 = {3,4,5,6}

s1.union(s2)            # {1,2,3,4,5,6}      → all elements
s1.intersection(s2)     # {3,4}              → common elements
s1.difference(s2)       # {1,2}              → in s1 not in s2
s1.symmetric_difference(s2)  # {1,2,5,6}    → not common
s1.issubset(s2)         # True/False → s1 inside s2?
s1.issuperset(s2)       # True/False → s1 contains s2?
s1.isdisjoint(s2)       # True/False → no common elements?


s1 | s2    # union
s1 & s2    # intersection
s1 - s2    # difference
s1 ^ s2    # symmetric difference

s = {5, 3, 1, 4, 2}
len(s)      # 5
max(s)      # 5
min(s)      # 1
sum(s)      # 15
sorted(s)   # [1,2,3,4,5] → returns list!

#1 
set1 = {1,2,3,4,5}

print(3 in set1)

print("_"*50)
print("_"*50)

#2

set2 = {1,2,3,4,5}
print(set2)
print(len(set2))

print("_"*50)
print("_"*50)

#3
set3 = set()

set3.add(6)
print(set3)

set3.add(7)
print(set3)



print("_"*50)
print("_"*50)

#4
set4 = {1,2,3,4,5,6,7,8,9,0}
set4.remove(5)
print(set4)
set4.discard(5)
print(set4)

print("_"*50)
print("_"*50)

#5

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.union(s2))
print(s1 | s2)


print("_"*50)
print("_"*50)

#6

print(s1.intersection(s2))
print(s1&s2)


#7

print(s1.difference(s2))
print(s2.difference(s1))
print(s1-s2)
print(s2-s1)

print("_"*50)
print("_"*50)

#8

set8 = frozenset([1,2,3,4,5,6])
print(set8)

#set8.add(4)     
#set8.remove(1)   
#set8.clear() 


print("_"*50)
print("_"*50)


#9

list1 = [1,2,3,4,5,6,4,5,7]
print(set(list1))

list2 = [5,3,2,1,1,5,2,5]
seen  = set()
result = []

for i in list2:
    if i not in seen:
        result.append(i)
        seen.add(i)
print(result)



print("_"*50)
print("_"*50)

#10

set10 = {x*2 for x in range(1,11)}
print(set10)







