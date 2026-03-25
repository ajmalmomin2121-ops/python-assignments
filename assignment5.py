class BankAccount:
    def __init__(self,acc_no,bal):
        self.acc = acc_no
        self.balance = bal
    
    def deposit(self):
        amt = float(input("Enter amount to deposit:"))
        self.balance = self.balance + amt
        print("Deposited", amt)
            
    def withdraw(self):
        amt = float(input("Enter amount to withdraw:"))
        if amt <= self.balance:
            self.balance = self.balance - amt
            print("Withdraw:", amt)
        else:
            print("Not enough balance")
            
    def check_balance(self):
       print("Current balance:", self.balance)

acc = input("Enter Account number:")
bal = float(input("Enter initial balance:"))
obj = BankAccount(acc,bal)

while True:
    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Exit")
    
    ch = input("Enter choice:")
    
    if ch == "1":
        obj.deposit()
    elif ch == "2":
        obj.withdraw()
    elif ch == "3":
        obj.check_balance()
    elif ch == "4":
        print ("Thank You")
        break
    else:
        print("Wrong choice")
