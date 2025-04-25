from account import Account


class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def add_account(self, account: Account):
        self.accounts[account.account_number] = account

    def login(self, account_no, pin):

        account = self.accounts.get(account_no)

        if account and account.check_pin(pin):
            self.current_account = account
            print(f"\n✅ Welcome, {account.name}!\n")
            return True
        else:
            print("❌ Invalid account number or PIN.")
            return False

    def run(self):
        while True:
            acc_no = int(input("🔑 Enter Account Number: "))
            pin = input("🔒 Enter PIN: ")
            if self.login(acc_no, pin):
                self.show_menu()
                self.logout()
            else:
                retry = input("❓ Try again? (y/n): ").lower()
                if retry != 'y':
                    break

    def logout(self):
        print(f"\n👋 Goodbye, {self.current_account.name}!\n")
        self.current_account = None

    def show_menu(self):
        while True:
            print("\n📋 Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")

            choice = input("👉 Enter choice (1-5): ")

            try:
                if choice == '1':
                    self.current_account.check_balance()
                elif choice == '2':
                    amount = float(input("💵 Enter amount to deposit: "))
                    self.current_account.deposit(amount)
                elif choice == '3':
                    amount = float(input("💸 Enter amount to withdraw: "))
                    self.current_account.withdraw(amount)
                elif choice == '4':
                    old_pin = input("🔐 Enter current PIN: ")
                    new_pin = input("🔐 Enter new PIN: ")
                    self.current_account.change_pin(old_pin, new_pin)
                elif choice == '5':
                    break
                else:
                    print("❌ Invalid option.")
            except ValueError as e:
                print(f"⚠️ Error: {e}")
