# Question:
# Create a bank account system with deposit,
# withdraw and balance check.

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("Aashish", 10000)

acc.show_balance()

acc.deposit(5000)

acc.withdraw(3000)

acc.show_balance()