class dealars:
    def __init__(self, id, name, mobile, address):
        self.id= id
        self.name= name
        self.mobile = mobile
        self.address = address
        
    def display(self):
        print(self.id, self.name, self.mobile, self.address)
        
        
    def isPune(self):
        return self.address == "Pune"

    def isPalindrome(self,mobile):
        m = str(mobile)
        return m == m[::-1]   
    
    
    
d = [
    dealars(1, "Raj",   "12321",     "Pune"),
    dealars(2, "Sam",   "98789",     "Mumbai"),
    dealars(3, "Priya", "45654",     "Pune"),
    dealars(4, "John",  "11111",     "Delhi"),
    dealars(5, "Neha",  "98901",     "Pune")
]


print("ALL : ")
for i in d:
    i.display()

print("*"*30)           
print("PuneWale : ")
for i in d:
    if i.isPune():
        print(i.name, i.address)
        
print("*"*30)        
print("Palindrome Wale : ")
for i in d:
    if i.isPalindrome(i.mobile):
        print(i.name, i.mobile)
    
    
    