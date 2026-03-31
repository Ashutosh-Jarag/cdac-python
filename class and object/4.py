class bankAccount:
    def __init__(self, ano, name, balance):
        self.ano = ano
        self.name = name
        self.balance = balance
        
    def display(self):
        print(self.ano, self.name, self.balance)
        
    def deposit(self,amount):
        if amount<=0:
            print("INVALID")
        else:
            self.balance+=amount
            
            print(amount)
            print(self.balance)
            
    def withdraw(self,amount):
        if amount<=0:
            print("INVALID")
        elif(amount> self.balance):
            print("INSUFFICINT BALANCE")
        else:
            self.balance-=amount            
            print(amount)
            print(self.balance)
            
    def display_balance(self):
        return self.balance
        
    
b = bankAccount(1, "raj", 20000)
b.display()
b.deposit(00)





