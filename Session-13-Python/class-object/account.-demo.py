class Account:
    # here 0 is the default value in case if you are not giving any balance
    def __init__(self, acc_no, owner, balance=0):
        self.acc_no=acc_no
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}. New Balance:  {self.balance}")
        else:
            print("Diposit amount must be Positive")
        
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            print(f"Withdrew {amount}. Remaining Balance:  {self.balance}")
        else:
            print("Insifficient balance or invalid amount!")
            
    def display_balance(self):
        print(f"Account holder: {self.owner}, Balance: {self.balance}")
        
# Usage
acc1= Account("SBI0000001","Sonam Soni",5000)

acc1.display_balance()
acc1.deposit(1500)
acc1.withdraw(2000)
acc1.withdraw(6000)