
import random

class Account(object):
    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f'Current balance is {self.current_balance}')


    def withdraw(self, ammount):
        self.current_balance = self.current_balance - float(ammount)
        print(f"New balance after withdraw is {self.current_balance}")


    def deposit(self):
        self.current_balance = self.current_balance + float(ammount)
        print(f"New balance after deposit is {self.current_balance}")

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):   # __ means it is a private method
        print(f'Amount of balance from the db for {self.user_id}')
        return random.randint(100,1000)

account1 = Account(987)
account1.withdraw(50)
