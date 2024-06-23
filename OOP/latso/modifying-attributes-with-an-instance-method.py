class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

account1 = BankAccount()
print(account1.deposit(50))
print(account1.withdraw(30))
print(account1.withdraw(200))
            
'''
Create a class BankAccount with an attribute balance. Define an instance method deposit that takes an amount and adds it to the balance, and another method withdraw that takes an amount and substracts it from the balance if there are sufficient funds!
'''