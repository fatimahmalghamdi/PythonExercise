class BankAccount:

    def __init__(self,balance=0):
        if balance == 0:
            self.balance = 0
        else:
            self.balance = balance
            self.interest_rate = balance - 1/100
            self.yieldInterest = 0
    
    def deposite(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.yieldInterest = self.balance * self.interest_rate
            self.balance = self.yieldInterest
            return self



account1 = BankAccount(1000)
account2 = BankAccount(200)

account1.deposite(1000).deposite(500).deposite(3000).withdraw(300).yield_interest().display_account_info()
account2.deposite(100).deposite(50).withdraw(10).withdraw(20).withdraw(30).withdraw(10).yield_interest().display_account_info()


