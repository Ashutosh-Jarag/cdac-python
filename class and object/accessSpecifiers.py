class Employee:
    def __init__(self, name, salary, password):
        self.name      = name        # public
        self._salary   = salary      # protected
        self.__password = password   # private
    
    def display(self):
        print(f"Name    : {self.name}")       # ✅
        print(f"Salary  : {self._salary}")    # ✅
        print(f"Password: {self.__password}") # ✅

e = Employee("Rahul", 50000, "rahul123")

# public ✅
print(e.name)         # Rahul

# protected ⚠️
print(e._salary)      # 50000 works but not recommended!

# private ❌
#print(e.__password)   # AttributeError!

print(e._Employee__password)

# correct way to access private
e.display()           # use method ✅

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    # getter
    def getBalance(self):
        return self.__balance
    
    # setter
    def setBalance(self, amount):
        if amount < 0:
            print("Invalid amount!")
        else:
            self.__balance = amount

acc = BankAccount(10000)
print(acc.getBalance())    # 10000 ✅
acc.setBalance(20000)
print(acc.getBalance())    # 20000 ✅
acc.setBalance(-500)       # Invalid amount!