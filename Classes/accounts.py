import random 
import pdb 

class Account(object):

    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_databases()
        print(self.current_balance)
        print(f"Current Balance is: {self.current_balance}")
    
    def withdraw(self, amount):
        self.current_balance = self.current_balance - float (amount)
        print(f"New Balance after withdraw is: {self.current_balance}")

    def deposit(self, amount):
        self.current_balance = self.current_balance + float (amount)
        print(f"Current Balance after deposit is: {self.current_balance}")

    def generate_statement(self):
        pass    

    def __read_balance_from_databases(self):
        print(f"Getting balance from db for", self.user_id)
        return random.randint(100, 1000)


account = Account(98769)   


pdb.set_trace()