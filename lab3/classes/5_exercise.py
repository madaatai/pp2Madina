class BankAccount:
    def __init__(self, account, balance):
        self.account=account
        self.balance=balance
    def owner(self):
        return self.account
    def money(self):
        return self.balance
    def deposite(self, addition):
        if addition>0:
            self.balance+=addition
            print(f"You added {addition} $, your balance are {self.balance} $")
        else:
            print("Sum of deposite should be positive !")
    def withdraw(self, taken):
        if self.balance-taken<0:
            print("You dont have enough money for this operation !")
        elif self.balance-taken>=0:
            self.balance-=taken
            print(f"Your balance are {self.balance} $, you take {taken} $")
        else:
            print("Please enter the valid value !")

my_bankacc=BankAccount("Rauan", 10000)
print(my_bankacc.owner())
print(f"{my_bankacc.money()} $")
my_bankacc.deposite(15000) #You added 15000 $, your balance are 25000 $
my_bankacc.withdraw(5000) #Your balance are 20000 $, you take 5000 $
my_bankacc.withdraw(30000) #You dont have enough money for this operation !