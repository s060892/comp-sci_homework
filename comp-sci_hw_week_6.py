"""
UML- BankAccount

- forename : String
- surname : String
- balance : Float
- transactionHistory : List[String]
- withdraw(amount: Float)
- deposit(amount: Float)

"""


class BankAccount:
    #CONSTRUCTOR METHOD - sets up the INSTANCE of a class
    def __init__(self, forename, surname, starting_balance=0):
        self.forename = forename
        self.surname = surname
        self.balance = starting_balance
        self.transactionHistory = []

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = round(self.balance - amount, 2)
            self.transactionHistory.append(f"Withdrew: {amount:.2f}")
        else:
            print("Insufficient funds in account")
        print(f"Account balance: {self.balance}")

    def deposit(self, amount):
        self.balance = round(self.balance + amount, 2)
        self.transactionHistory.append(f"Deposited: {amount:.2f}")
    
Nour_account = BankAccount("Nour", "Mishreky", 100)  
Nour_account.withdraw(20.19)
Nour_account.deposit(10.45)
Nour_account.withdraw(20.19)
Nour_account.withdraw(20.19)
Nour_account.withdraw(20.19)
Nour_account.withdraw(20.19)
Nour_account.withdraw(20.19)
print("Transaction history:", Nour_account.transactionHistory)
