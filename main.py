import time
import random
import json

class Bank_Account():
    def __init__(self, account_No, fName, bank_Amount=0):
        self.account_No = account_No
        self.fName = fName
        self.bank_Amount = bank_Amount

    def get_account_No(self):
        return self.account_No
    
    def get_fName(self):
        return self.fName

    def deposit_Money(self, amount):
        bank_Amount += amount
    
def main():
    slow_text("ATM.... Press any key to continue.\n>>")
    input()
    slow_text("\nNavigation:\nC >> Create Account\nL >> Login\n>>")
    try:
        nav = input()
    except:
        print("Invalid.")
    
    if nav == "C" or "c":
        slow_text("Enter your Full Name \n>>")
        full_Name = input()
        account_No = random.randint(1000,9999)
        account = Bank_Account(account_No, full_Name)

        with open("bank.json", "w") as f:
            json.dump(account.account_No, f)




def slow_text(text):
    text = list(text)
    for i in text:
        print(i, end="", flush = True)
        time.sleep(0.05)

main()