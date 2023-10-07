import random 
import pdb 


class DatabaseHeper:
    
    def __init__(self, database_address, username, password):
        self.connection = "I ma just testing"

    def write_to_db(self):
        print('writing to db...')

    def read_from_db(self):
        print('reading from db...')

# example of Inhereitance
class Account(DatabaseHeper):

    def __init__(self, database_address, username, password, user_id, currency='USD'):
        super().__init__(database_address, username, password)
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
    
    def __write_balance_to_databases(self):
        print('Reading balance from db from db')

        
# example of composition
class Account(object):

    def __init__(self, user_id, database_address, username, password, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_databases()
        print(self.current_balance)
        print(f"Current Balance is: {self.current_balance}")
        self.db_helper = DatabaseHeper(database_address, username, password)
    
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
        self.db_helper.read_from_db()
        return random.randint(100, 1000)
    
    def __write_balance_to_databases(self):
        print('Reading balance from db from db')
        self.db_helper.write_to_db()