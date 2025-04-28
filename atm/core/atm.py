import os
from atm.models import User, Account
from atm.core.crypto_manager import CryptoManager


class ATM:
    def __init__(self):
        self.crypto = CryptoManager()
        self.users = self.load_users()
        self.current_user = None
        self.current_account = None

    def load_users(self):
        data = self.crypto.load_from_file("data/users.dat")
        return {uid: User.from_dict(udata) for uid, udata in data.items()}

    def save_users(self):
        data = {uid: user.to_dict() for uid, user in self.users.items()}
        self.crypto.save_to_file("data/users.dat", data=data)

    def details(self):
        print(f"{self.current_account} {self.current_user}")

    def add_user(self, user: User):
        self.users[user.user_id] = user
        self.save_users()

    def add_user_interactively(self):
        user_id = input("🆔 Enter new user ID: ")
        name = input("👤 Enter name: ")
        role = input("👥 Role (user/admin): ").lower()
        account_number = int(input("🏦 Enter account number: "))
        pin = input("🔐 Enter PIN: ")
        balance = float(input("💰 Initial balance: "))

        new_user = User(user_id, name, role)
        new_account = Account(account_number, pin, balance)
        new_user.add_account(new_account)
        self.add_user(new_user)
        print("✅ User and account created successfully.")

    def login(self, user_id, account_no, pin):
        user = self.users.get(user_id)
        if not user:
            print("❌ User not found.")
            return False

        account = user.get_account(account_no)

        if account and account.check_pin(pin):
            self.current_account = account
            self.current_user = user
            print(f"\n✅ Welcome, {self.current_user.name}!\n")
            return True
        else:
            print("❌ Invalid account number or PIN.")
            return False

    def run(self):
        if not self.users:
            print("No User found in system. Create a New User and account.")
            self.add_user_interactively()
        else:
            while True:
                want_to_exit = input("Do you want to exit from system? (y/n):")
                if want_to_exit.lower() == 'y' or want_to_exit.lower() == 'yes':
                    break
                user_id = input("🆔 Enter user ID: ")
                acc_no = int(input("🏦 Enter account number: "))
                pin = input("🔒 Enter PIN: ")
                if self.login(user_id, acc_no, pin):
                    self.show_menu()
                    self.logout()
                else:
                    retry = input("❓ Try again? (y/n): ").lower()
                    if retry != 'y':
                        break

    def logout(self):
        print(f"\n👋 Goodbye, {self.current_user.name}!\n")
        self.current_account = None
        self.current_user = None

    def list_users(self):
        print(f"User No - Name - Role")
        for user_no, user in self.users.items():
            print(f"{user_no} - {user.name} - {user.role}")

    def show_menu(self):
        while True:
            print("\n📋 Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")
            if self.current_user.is_admin():
                print("6. Add User")
                print("7. List Users")

            choice = input("👉 Enter choice (1-7): ")

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
                elif choice == '6' and self.current_user.is_admin():
                    self.add_user_interactively()
                elif choice == '7' and self.current_user.is_admin():
                    self.list_users()
                else:
                    print("❌ Invalid option.")
            except ValueError as e:
                print(f"⚠️ Error: {e}")
