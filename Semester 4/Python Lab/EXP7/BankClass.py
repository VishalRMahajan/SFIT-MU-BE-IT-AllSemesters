"""Write a python program to create a Bank class where deposits and withdrawals can
be handled by using instance methods."""

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance

    def display(self):
        print("\nBank Details:")
        print("Balance:", self.balance)


balance = int(input("\nEnter the initial balance: "))
Bank_obj = Bank(balance)

amount = int(input("\nEnter the amount to be deposited: "))
print("Balance after deposit:", Bank_obj.deposit(amount))

amount = int(input("\nEnter the amount to be withdrawn: "))
print("Balance after withdrawal:", Bank_obj.withdraw(amount))

Bank_obj.display()
