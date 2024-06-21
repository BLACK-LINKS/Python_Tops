class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",cname," Your account is opened. ",acno," This is your account number with ",balance," rs.")  
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,withdraw):
        if amount<=self.balance:
            self.balance-=amount
            file=open(acno+".txt", "w")
            amount=str(amount)
            file.write("Withdraw Amount: ",amount)
            file.close()
                
        else:
            print("Insufficient Balance ",amount-self.balance, " rs. More is required. ")

    def checkbalance(self):
        self.balance
    
        
b1=Bank()
acno=int(input("Enter Account Number : "))
cname=input("Enter Acc Holder Name : ")
balance=int(input("Enter Initial Balance : "))

b1.openAccount(acno,cname,balance)

while True:
    print("*********************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*********************************")

    choice=int(input("Enter your choice: "))
    print("*********************************")

    if choice==1:
        amount=int(input("Enter Deposit Amount: "))
        b1.deposit(amount)
        
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount: "))
        b1.withdraw(amount)

    elif choice==3:
        b1.checkbalance()

    elif choice==4:
        print("Thank you for using our Services. ")
        break

    else:
        print("Invalid Choice, Please Try again!!")


