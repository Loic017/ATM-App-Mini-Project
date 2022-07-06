from re import A
import time
import random
import json

class Bank_Account():
    def __init__(self, account_No, fName, user_password, bank_Amount=0):
        self.account_No = account_No
        self.fName = fName
        self.bank_Amount = bank_Amount
        self.user_password = user_password

    def get_account_No(self):
        return self.account_No
    
    def get_fName(self):
        return self.fName

    def deposit_Money(self, amount):
        bank_Amount += amount
    
def main():
    slow_text("ATM.... Press any key to continue.\n>> ")
    input()
    slow_text("\nNavigation:\nC >> Create Account\nL >> Login\n>> ")
    nav = input()
    if nav == "C":
        create_account()
    elif nav == "L":
        login()
    else:
        slow_text("Invalid Selection.")

def load_json():
    try:
        with open("bank.json", "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def save_json(data):
    with open("bank.json", "w") as f:
        json.dump(data, f)

def create_account():
    loaded = load_json()

    slow_text("Enter your Full Name \n>> ")
    full_Name = input()
    account_No = random.randint(1000,9999)

    slow_text("Enter a Password \n>> ")
    user_password = input()
    user_password = user_password.encode("utf-8").hex()

    account = Bank_Account(account_No, full_Name, user_password)

    save_list = {"account_fullname": account.get_fName(),"account_password": account.user_password,"account_bankAmount": account.bank_Amount}
    loaded[account.get_account_No()] = save_list
    save_json(loaded)
    

    slow_text(f"Account Created.\nThis is your account number: {account_No}\n")
    main()

def login():
    slow_text("Enter your Account Number \n>> ")
    account_Number = input()
    slow_text("Enter your Password \n>> ")
    login_password = input()

    bank_data = load_json()
    try:
        if bank_data[account_Number]["account_password"] == (login_password.encode("utf-8").hex()):
            print('true')
    except:
        print("Incorrect Login, Please Try Again.")
        login()
    
def slow_text(text):
    text = list(text)
    for i in text:
        print(i, end="", flush = True)
        time.sleep(0.025)

main()