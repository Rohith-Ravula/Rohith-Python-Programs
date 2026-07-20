# Write a program for Banking application.
# Take input from the user to check balance, Deposit amount and Withdraw amount
# we should create 3 function i) for Checking balance, ii) Deposit amount, iii) Withdraw amount
from random import randint
print("Welcome to Nagaram Bank")
Acc_num=randint(1001,9999)
balance=0
kyc_doc={}
def create_account():
    print("Please provide user details to open a new bank account with us")
    Name=input("Enter your name: ")
    print(f"Thanks {Name} for banking with us. Your Account Number is {Acc_num}")


def check_balance():
    print("Enter your account details")
    print()
    num=int(input("Enter your 4 digit account number: "))
    if num==Acc_num:
        print(f"Your current account balance is: {balance}")
        print()
    else:
        print("Please enter valid account number")
        print()

def deposit_amount():
    global balance
    print("Enter your account details")
    print()
    num= int(input("Enter your 4 digit account number: "))
    if num==Acc_num:
        amount=int(input("Enter amount to be deposited: "))
        if amount<=0:
            print("Cannot deposit negative or zero amount")
            print()
        else:
            balance+=amount
            print(f"Amount {amount} credited successfully")
            print(f"Your current account balance is {balance}")
            print()
    else:
        print("Please enter valid account number")
        print()




def withdraw_amount():
    global balance
    print("Enter your account details")
    print()
    num= int(input("Enter your 4 digit account number: "))
    if num==Acc_num:
        amount=int(input("Enter amount to be withdrawn: "))
        if amount>balance:
            print(f"Insufficient balance. You have only {balance} left")
            print()
        elif amount<0:
            print("Cannot withdraw negative or zero amount")
        else:
            balance-=amount
            print(f"Amount {amount} withdrawn successfully")
            print(f"Please collect withdrawn amount {amount} from near by ATM. !HAHA!")
    else:
        print("Please enter valid account number")

def check_kyc(**docs):
    if len(kyc_doc)==0:
        print("No KYC done")
    else:
        for docs in kyc_doc:
            print(f"The provided KYC docs are {docs}: {kyc_doc[docs]}")

def update_kyc(docs):
    global kyc_doc
    kyc_doc.update(docs)

if __name__=="__main__":
    while True:
        print("Choose the below options from 1 to 7 to bank with us")
        print("1. Create a new bank account with us")
        print("2. Check Balance")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Check KYC")
        print("6. Update KYC")
        print("7. Exit")
        choice=(input("Enter your choice: "))
        if choice=='1':
            create_account()
        elif choice=='2':
            check_balance()
        elif choice=='3':
            deposit_amount()
        elif choice=='4':
            withdraw_amount()
        elif choice=='5':
            check_kyc()
        elif choice=='6':
            kyc_docs = {}
            n_doc = int(input("Enter number of docs to be added: "))
            for i in range(n_doc):
                key = input("Enter the type of the document: ")
                value = input("Enter the document serial number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("KYC is updated successfully")

        elif choice=='7':
            print("Quitting. Have a nice day!")
            break
        else:
            print("Please enter a valid choice. Select from 1 to 7 options")
print("Thank you for banking with us!!")


#Banking application:
# print("Welcome to ABC Bank")
# balance=0
# def deposit():
#     global balance
#     amount=int(input("Enter amount to deposit: "))
#     balance+=amount





