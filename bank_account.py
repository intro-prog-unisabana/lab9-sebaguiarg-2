# bank_account.py

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        
        self.account_number = account_number
        self.balance = float(balance)

    def deposit(self, amount):
        
        self.balance += amount

    def withdraw(self, amount):
        
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount
            return 0

    def __str__(self):
        acc_str = str(self.account_number)
        last_two = acc_str[-2:]
        
        return (f"Account Number: **{last_two}\n"
                f"Current Balance: {self.balance:.1f}")
