class User:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.bankAccount = 0


    def display_user_balance(self):
        print(f"The user name is: {self.name} and have balance: ${self.bankAccount}")

    def make_withdrawal(self,amount):
        self.bankAccount -= amount
    
    def makeDeposite(self,money):
        self.bankAccount += money
        # self.display_user_balance()
    
    def transfer_money(self, amount):
        self.bankAccount -= amount
        self.display_user_balance()



person1 = User("Fatimah",20)
person2 = User("Razan",25)
person3 = User("Khulud",30)

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

