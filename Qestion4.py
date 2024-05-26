#Question4 :

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance . ")
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number : {self.account_number}\n Username : {self.account_holder}\n Balance : {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
    
    def __str__(self):
        return f"Account Number :{self.account_number}\n Username : {self.account_holder}\n Balance : {self.balance}\n Interest :  {self.interest_rate}%"



bank_account = BankAccount("2910", "Saleh Shhela")


bank_account.deposit(1000)
print(bank_account)


bank_account.withdraw(500)
print(bank_account)


savings_account = SavingsAccount("01111", "Saleh Marwan ", 5)
savings_account.deposit(11000)

savings_account.apply_interest()
print(savings_account)
