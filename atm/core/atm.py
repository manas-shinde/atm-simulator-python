from atm.models import User, Account
import sqlite3

class ATM:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.current_user = None
        self.current_account = None

    def details(self):
        print(f"{self.current_account} {self.current_user}")

    def add_user(self, user: User, account: Account):
        with self.conn:
            self.conn.execute(
                "INSERT INTO users (user_id, name, role) VALUES (?, ?, ?)",
                (user.user_id, user.name, user.role)
            )
            account.create_account(account.account_number, account._Account__pin, account.balance, user.user_id)
        print("✅ User and account created successfully.")

    def add_user_interactively(self):
        user_id = input("🆔 Enter new user ID: ")
        name = input("👤 Enter name: ")
        role = input("👥 Role (user/admin): ").lower()
        account_number = input("🏦 Enter account number: ")
        pin = input("🔐 Enter PIN: ")
        balance = float(input("💰 Initial balance: "))

        new_user = User(user_id, name, role)
        new_account = Account(self.conn)
        new_account.account_number = account_number
        new_account._Account__pin = pin
        new_account.balance = balance

        self.add_user(new_user, new_account)

    def login(self, user_id, account_no, pin):
        cur = self.conn.execute("SELECT name, role FROM users WHERE user_id = ?", (user_id,))
        user_row = cur.fetchone()
        if not user_row:
            print("❌ User not found.")
            return False

        # Validate account and pin
        account = Account(self.conn)
        if account.check_pin(account_no, pin):
            self.current_user = User(user_id, user_row[0], user_row[1])
            self.current_account = account
            self.current_account.account_number = account_no
            print(f"\n✅ Welcome, {self.current_user.name}!\n")
            return True
        else:
            print("❌ Invalid account number or PIN.")
            return False

    def run(self):
        while True:
            user_id = input("🆔 Enter user ID: ")
            acc_no = input("🏦 Enter account number: ")
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
        print(f"User ID - Name - Role")
        cur = self.conn.execute("SELECT user_id, name, role FROM users")
        for user_id, name, role in cur.fetchall():
            print(f"{user_id} - {name} - {role}")

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
                    self.current_account.check_balance(self.current_account.account_number)
                elif choice == '2':
                    amount = float(input("💵 Enter amount to deposit: "))
                    self.current_account.deposit(self.current_account.account_number, amount)
                elif choice == '3':
                    amount = float(input("💸 Enter amount to withdraw: "))
                    self.current_account.withdraw(self.current_account.account_number, amount)
                elif choice == '4':
                    old_pin = input("🔐 Enter current PIN: ")
                    new_pin = input("🔐 Enter new PIN: ")
                    self.current_account.change_pin(self.current_account.account_number, old_pin, new_pin)
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
