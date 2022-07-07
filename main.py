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
        self.bank_Amount += amount
    
    def withdraw_Money(self, amount):
        self.bank_Amount -= amount
    
def main():
    slow_text("ATM.... Press any key to continue.\n>> ")
    input()
    slow_text("\nNavigation:\nC >> Create Account\nL >> Login\n>> ")
    nav = input()
    if nav == "C":
        create_account()
    elif nav == "L":
        try:
            login()
        except:
            slow_text("Invalid Login.")
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
    
    if bank_data[account_Number]["account_password"] == (login_password.encode("utf-8").hex()):
        account(account_Number, bank_data[account_Number]["account_fullname"], login_password, bank_data, bank_data[account_Number]["account_bankAmount"])
    
def account(number, name, password, data, amount):
    slow_text(f"\nWelcome, {name}.")
    slow_text("\nWould you like to...\nCheck Balance >> C\nDeposit >> D\nWithdraw >> W\nSign Out >> S")
    navigate = input("\n>> ")
    current_account = Bank_Account(number, name, password, amount)

    bank_data = load_json()

    if navigate == "D":
        bank_data = load_json()
        slow_text("How much would you like to deposit?")
        input_amount = int(input("\n>> "))
        current_account.deposit_Money(input_amount)
        slow_text("Making the deposit......")
        bank_data[number]["account_bankAmount"] = current_account.bank_Amount
        save_json(bank_data)
        slow_text("\nDeposit Completed.")
        slow_text(f"\nYour balance is {current_account.bank_Amount}.")
        account(number, name, password, data, amount)
    elif navigate == "W":
        bank_data = load_json()
        slow_text("How much would you like to withdraw?")
        input_amount = int(input("\n>> "))
        current_account.withdraw_Money(input_amount)
        slow_text("Making the withdraw......")
        bank_data[number]["account_bankAmount"] = current_account.bank_Amount
        save_json(bank_data)
        slow_text("\nWithdraw Completed.")
        slow_text(f"\nYour balance is {current_account.bank_Amount}.")
        account(number, name, password, data, amount)
    elif navigate == "C":
        bank_data = load_json()
        check_am = bank_data[number]["account_bankAmount"]
        slow_text(f"Your balance is {check_am}.")
        account(number, name, password, data, amount)
    elif navigate == "S":
        slow_text("Signing out.")
    else:
        slow_text("Invalid input entered.")
        account(number, name, password, data, amount)

def slow_text(text):
    text = list(text)
    for i in text:
        print(i, end="", flush = True)
        time.sleep(0.025)

main()