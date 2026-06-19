# Question:
# Create a BankAccount class.
#
# Implement:
# 1. Deposit Amount
# 2. Withdraw Amount
# 3. Check Balance
#
# Display appropriate message for insufficient balance.
#
# Topic:
# OOPs, Class, Object, Methods

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)

account = BankAccount("Aashish", 10000)

account.check_balance()

account.deposit(5000)

account.withdraw(3000)

account.check_balance()