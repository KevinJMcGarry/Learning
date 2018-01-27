import datetime
import pytz  # this is used to store date/time in utc format

class Account(object):
    """ Simple Account class with balance"""  # good practice to include a docstring at start of class

    @staticmethod  # defining that the following method is static - used by all instances and doesn't require self parameter
    def _current_time():
        utc_time = datetime.datetime.utcnow()  # storing datetime in utc format
        return pytz.utc.localize(utc_time)  # returning localized datetime as well

    def __init__(self, name, balance):  # init method initializes the class with attributes
        self.name = name  # all methods take self as their first parameter
        self.balance = balance
        self.transaction_list = []  # initializing an empty list to store transactions info for deposits and withdrawals
        print("account created for {}".format(self.name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))  # uses static method for date/time
            # details for the transaction stored as a tuple in the list

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
        # if 0 < amount <= self.balance:  # short hand way of writing the above statement
            self.balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))  # notice the negative amount for withdrawal
        else:
            print("The amount must be greater than 0 and no more than your balance of {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1  # converting amount to a negative number for withdrawal
            print("{:6} {} on {} (local time was {})".format(amount, transaction_type, date, date.astimezone()))


    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    kevin = Account("Kevin", 50000)
    kevin.show_balance()
    kevin.deposit(15000)
    kevin.withdrawal(3000)
    kevin.show_transactions()
