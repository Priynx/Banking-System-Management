import re 


class Account:

    def __init__(self, account_no, balance,pin,name,gmail):
        self.account_no = account_no
        self.balance = balance
        self.pin = pin
        self.name = name
        self.gmail = gmail
        self.transaction = []

    def validate_email(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, self.gmail):
            return True
        else:
            return False

    def validate_name1(self):
        pattern = r"^[A-Za-z ]+$"
        if re.match(pattern, self.name):
            return True
        else:
            return False

    def validate_pin(self):
        pattern = r"^[0-9]{4}$"

        if re.match(pattern, self.pin):
            return True
        else:
            return False

    def validate_account_no(self):
        pattern = r"^[0-9]{6}$"

        if re.match(pattern, self.account_no):
            return True
        else:
            return False
 
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print("Rs.", amount, "was debited")
            self.transaction.append(f"Rs. {amount} was debited")

    def credit(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        else:
            self.balance += amount
            print("Rs.", amount, "was credited")
            self.transaction.append(f"Rs. {amount} was credited")

    def bal(self):
        print("Balance: Rs.", self.balance)

    def trans(self):
        print("\nTransaction History:")
        for i in self.transaction:
            print(i)


accounts = []

while True:

    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_no = input("Enter account number: ")
        Name= input("Enter your name: ")
        pin = input("Enter PIN: ")
        gmail=input("Enter your gmail:")
        new_account = Account(account_no, 0,pin,Name,gmail)
        
        if new_account.validate_account_no() and new_account.validate_name1() and new_account.validate_pin() and new_account.validate_email():
            accounts.append(new_account)
            print("Account created successfully!")
        else:
            print("Invalid details")


    elif choice == "2":

        account_no = input("Enter account number: ")
        pin = input("Enter PIN: ")
        logged_in = False

        for account in accounts:

            if account.account_no == account_no and account.pin == pin:

                logged_in = True
                print("Login successful!")

                while True:

                    print("\n===== ACCOUNT MENU =====")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Logout")

                    option = input("Enter your choice: ")

                    if option == "1":
                        amount = float(input("Enter amount: "))
                        account.credit(amount)

                    elif option == "2":
                        amount = float(input("Enter amount: "))
                        account.debit(amount)

                    elif option == "3":
                        account.bal()

                    elif option == "4":
                        account.trans()

                    elif option == "5":
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice")

                break

        if logged_in == False:
            print("Account not found")

    elif choice == "3":
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid choice")