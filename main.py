from atm import ATM, Account

if __name__ == "__main__":
    atm = ATM()

    # Add sample accounts
    atm.add_account(Account(1001, "Alice", "1234", 5000.0))
    atm.add_account(Account(1002, "Bob", "5678", 3000.0))

    print("🏧 Welcome to Python Bank ATM\n")
    atm.run()
