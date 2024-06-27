class BankAccount:
    def __init__(self, ID, money):
        self.ID = ID
        self.money = money
    def withdraw(self, amount):
        if (self.money - amount < 0):
            print("Insufficient funds!")
        else:
            self.money -= amount
            print("Your balance is: " + str(self.money))
    def deposit(self, amount):
        self.money += amount
        print("Your balance is: " + str(self.money))

Account1 = BankAccount("12387621386", 1000)
Account2 = BankAccount("12039823798", 0)

print(Account1.money)
print(Account2.money)

Account1.withdraw(500)
Account2.deposit(500)
Account2.withdraw(10000)

