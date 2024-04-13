class Account:
    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = 50  # Default balance set to $50

    def deposit(self, amount):
        """Method to deposit money into the account."""
        self.balance += amount
        print(f"You have deposited ${amount}. Your balance is ${self.balance}")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn ${amount}. Your balance is ${self.balance}")
        else:
            print("Your balance is insufficient for the transaction")

    def get_balance(self):
        """Method to check the current balance of the account."""
        print(f"Your account balance is ${self.balance}")

    def __str__(self):
        """String representation of the account."""
        return f"Account Number: {self.account_number}, Account Name: {self.account_name}, Balance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_number, account_name, interest_rate):
        super().__init__(account_number, account_name)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Method to calculate and add interest to the account balance."""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest calculated. Your balance is now ${self.balance}")

    def __str__(self):
        """String representation of the savings account."""
        return f"Savings Account - {super().__str__()}, Interest Rate: {self.interest_rate}%"


class CurrentAccount(Account):
    def __init__(self, account_number, account_name, overdraft_limit):
        super().__init__(account_number, account_name)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):
        """Method to check if the account has exceeded its overdraft limit."""
        if self.balance <= 0 and abs(self.balance) > self.overdraft_limit:
            print("You have exceeded your overdraft limit")
        else:
            print("You are within your overdraft limit")

    def __str__(self):
        """String representation of the current account."""
        return f"Current Account - {super().__str__()}, Overdraft Limit: {self.overdraft_limit}"


class Bank:
    def __init__(self):
        self.list_of_accounts = []  # Initialize an empty list to store accounts

    def add_account(self, account):
        """Method to add an account to the bank."""
        self.list_of_accounts.append(account)

    def remove_account(self, account):
        """Method to remove an account from the bank."""
        self.list_of_accounts.remove(account)

    def view_all_accounts(self):
        """Method to view details of all accounts in the bank."""
        for account in self.list_of_accounts:
            print(account)

    def account_menu(self, account):
        """Method to provide a menu for interacting with a specific account."""
        while True:
            print("\nAccount Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Back to homepage")

            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                account.get_balance()
            elif choice == '4':
                print("\nWelcome back")
                break
            else:
                print("Invalid choice. Please try again.")


# Main bank menu
def main_menu():
    # Create instances of accounts
    kofi = Account(101, "Kofi")
    ama = SavingsAccount(102, "Ama", 5)
    kwame = CurrentAccount(103, "Kwame", 2000)

    # Create an instance of the Bank
    bank = Bank()

    # Add accounts to the bank
    bank.add_account(ama)
    bank.add_account(kofi)
    bank.add_account(kwame)
    while True:
        print("\nBank Menu:")
        print("1. View All Accounts")
        print("2. Access Account")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bank.view_all_accounts()
        elif choice == '2':
            account_number = input("Enter account number: ")
            for account in bank.list_of_accounts:
                if str(account.account_number) == account_number:
                    bank.account_menu(account)
                    break
            else:
                print("Account not found.")
        elif choice == '3':
            print("Exiting bank application...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
