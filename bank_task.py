import random
class Bank:
    def __init__(self):
        self.acno = None
        self.cname = None
        self.balance = None

    def openAccount(self, cname, balance):
        self.acno = random.randint(100000, 999999)  # Generate 6-digit random account number
        self.cname = cname
        self.balance = balance
        self.recordTransaction("Account Opened", balance)
        print("Hello ", cname, " Your account is opened. ", self.acno, " This is your account number with ", balance, " rs.")

    def deposit(self, amount):
        self.balance += amount
        self.recordTransaction("Deposit", amount)
        print("Deposit successful. New balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.recordTransaction("Withdraw", amount)
            print("Withdrawal successful. New balance:", self.balance)
        else:
            print("Insufficient Balance ", amount - self.balance,"rs. More is required. ")

    def checkbalance(self):
        self.recordTransaction("Check Balance", self.balance)
        print("Your current balance is:", self.balance)

    def recordTransaction(self, transactionType, amount):
        filename = str(self.acno) + ".txt"
        file = open(filename, "a")
        file.write(transactionType + ": " + str(amount) + "\n")
        file.close()

    def displayTransactions(self):
        filename = str(self.acno) + ".txt"
        file = open(filename, "r")
        print("Transaction History:")
        print(file.read())
        file.close()

b1 = Bank()

cname = input("Enter Acc Holder Name : ")
balance = int(input("Enter Initial Balance : "))

b1.openAccount(cname, balance)

while True:
    print("*********************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*********************************")

    choice = int(input("Enter your choice: "))
    print("*********************************")

    if choice == 1:
        amount = int(input("Enter Deposit Amount: "))
        b1.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter Withdrawal Amount: "))
        b1.withdraw(amount)

    elif choice == 3:
        b1.checkbalance()

    elif choice == 4:
        b1.recordTransaction("Exit", 0)  # Record system exit
        b1.displayTransactions()  # Display transaction history
        print("Thank you for using our Services. ")
        break

    else:
        print("Invalid Choice, Please Try again!!")
