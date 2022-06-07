
class BankAccount:

    def __init__(self,balance=0,accountNumber=0):
        if balance == 0:
            self.balance = 0
            self.accountNumber = accountNumber
        else:
            self.balance = balance
            self.accountNumber = accountNumber
            self.interest_rate = balance - 1/100
            self.yieldInterest = 0
    
    def deposite(self,amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
    
    def display_account_info(self):
        return self.balance
    
    def yield_interest(self):
        if self.balance > 0:
            self.yieldInterest = self.balance * self.interest_rate
            self.balance = self.yieldInterest



class User:

    def __init__(self,name,email,balance,accountNumber):
        self.name = name
        self.email = email
        self.accountNumber = accountNumber
        self.balance = balance
        self.account = BankAccount(self.balance,self.accountNumber)
    
    def makeNewAccount(self,balance,newAccountNumber):
        self.newUserBankAccount = BankAccount(balance,newAccountNumber)


    def display_user_balance(self):
        # print(f"The user name is: {self.name} and have balance: ${self.account.display_account_inf()}")
        print("The user name is: {} and have balance: $ {}".format(self.name , self.account.display_account_info()))

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def makeDeposite(self,money):
        self.account.deposite(money)
    
    def transfer_money(self, amount):
        self.account.withdraw(amount)
        self.display_user_balance()



#  user: Fatimah has 2 accounts
mydic = [
    {'name': 'Fatimah', 'email': 'fatimah@hotmail', 'balance': 1000, 'accountNumber': 123456},
    {'name': 'Fatimah', 'email': 'fatimah@hotmail', 'balance': 500, 'accountNumber': 111222},
    {'name': 'Razan', 'email': 'Razan@hotmail', 'balance': 5000, 'accountNumber': 223344},
    {'name': 'Khulud', 'email': 'Khulud@hotmail', 'balance': 2000, 'accountNumber': 101010}
]

person1 = User("Fatimah","fatimah@hotmail.com",1000,123456)
person2 = User("Razan","Razan@gmail.com",5000 , 223344)
person3 = User("Khulud","khulud@gmail.com",2000 , 101010)


# I was trying to solve the part of creating another account for same user, but did know how!!
print("choose 1 to open new account or 2 to open your existed account ")
choice = 1
if choice ==1:
    person1.makeNewAccount(100,1122334455)
else:
    print("provide your bank account number:")
    userInput = 111222
    # for x in range(0 , len(mydic)):
    #     if mydic[x]['accountNumber'] == userInput:


person1.makeDeposite(30000)
person1.makeDeposite(250000)
person1.makeDeposite(270000)
person1.make_withdrawal(10000)
person1.display_user_balance()

person2.makeDeposite(10000)
person2.makeDeposite(150000)
person2.make_withdrawal(5000)
person2.make_withdrawal(100)
person2.display_user_balance()

person3.makeDeposite(50000)
person3.make_withdrawal(1000)
person3.make_withdrawal(2000)
person3.make_withdrawal(3000)
person3.display_user_balance()

person1.transfer_money(1000)
person3.makeDeposite(1000)
person3.display_user_balance()

