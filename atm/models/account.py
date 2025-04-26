import hashlib
import sqlite3


class Account:
    def __init(self, conn: sqlite3.Connection):
        self.conn = conn

    def __init__(self, account_number: int, login_pin: str, balance: float = 1000.0):
        self.account_number = account_number
        self.__pin = login_pin
        self.balance = balance

    def create_account(self, account_no, pin, balance, user_id):
        with self.conn:
            self.conn.execute(
                "INSERT INTO accounts (account_no, pin, balance, user_id) VALUES (?, ?, ?, ?)",
                (account_no, pin, balance, user_id)
            )
        print(f"🏦 Account '{account_no}' created for user '{user_id}'")

    def deposit(self, account_no: str, amt: float):
        with self.conn:
            cur = self.conn.execute("SELECT balance FROM accounts WHERE account_no = ?", (account_no,))
            row = cur.fetchone()
            if row:
                new_balance = row[0] + amt
                self.conn.execute("UPDATE accounts SET balance = ? WHERE account_no = ?", (new_balance, account_no))
                print(f"✅ Deposited ₹{amt}. New balance: ₹{new_balance}.")
            else:
                print("❌ Account not found.")

    def withdraw(self, account_no: str, amt: float):
        with self.conn:
            cur = self.conn.execute("SELECT balance FROM accounts WHERE account_no = ?", (account_no,))
            row = cur.fetchone()
            if row:
                current_balance = row[0]
                if amt > current_balance:
                    print("❌ Insufficient balance!")
                else:
                    new_balance = current_balance - amt
                    self.conn.execute("UPDATE accounts SET balance = ? WHERE account_no = ?", (new_balance, account_no))
                    print(f"✅ Withdrawn ₹{amt}. New balance: ₹{new_balance}.")
            else:
                print("❌ Account not found.")

    def change_pin(self, account_no: str, old_pin: str, new_pin: str):
        with self.conn:
            cur = self.conn.execute("SELECT pin FROM accounts WHERE account_no = ?", (account_no,))
            row = cur.fetchone()
            if row:
                stored_hashed_pin = row[0]
                if stored_hashed_pin == self.hash_password(old_pin):
                    if stored_hashed_pin == self.hash_password(new_pin):
                        print("⚠️ New PIN can't be the same as the old one.")
                    else:
                        self.conn.execute(
                            "UPDATE accounts SET pin = ? WHERE account_no = ?",
                            (self.hash_password(new_pin), account_no)
                        )
                        print("✅ PIN updated successfully.")
                else:
                    print("❌ Old PIN is incorrect.")
            else:
                print("❌ Account not found.")

    def check_balance(self, account_no: str):
        cur = self.conn.execute("SELECT balance FROM accounts WHERE account_no = ?", (account_no,))
        row = cur.fetchone()
        if row:
            print(f"💰 Current Balance: ₹{row[0]}")
        else:
            print("❌ Account not found.")

    def check_pin(self, account_no: str, pin: str):
        cur = self.conn.execute("SELECT pin FROM accounts WHERE account_no = ?", (account_no,))
        row = cur.fetchone()
        if row:
            return row[0] == self.hash_password(pin)
        return False

    def hash_password(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f"Account Manager (DB Connection Active)"
