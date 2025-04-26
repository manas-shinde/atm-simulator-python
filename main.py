import sqlite3
from atm.core.atm import ATM
from atm.models import User, Account

def initialize_database(conn):
    """Creates users and accounts tables if they don't exist."""
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_no TEXT PRIMARY KEY,
                pin TEXT NOT NULL,
                balance REAL NOT NULL,
                user_id TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)

def insert_sample_data(atm):
    """Inserts a sample admin and user if they don't already exist."""
    # Check if sample admin exists
    cur = atm.conn.execute("SELECT * FROM users WHERE user_id = 'admin1'")
    if not cur.fetchone():
        admin = User("admin1", "Admin", "admin")
        admin_account = Account(atm.conn)
        admin_account.account_number = '9999'
        admin_account._Account__pin = '0000'
        admin_account.balance = 10000
        atm.add_user(admin, admin_account)

    # Check if sample user exists
    cur = atm.conn.execute("SELECT * FROM users WHERE user_id = 'user1'")
    if not cur.fetchone():
        user = User("user1", "Alice", "user")
        user_account = Account(atm.conn)
        user_account.account_number = '1001'
        user_account._Account__pin = '1234'
        user_account.balance = 5000
        atm.add_user(user, user_account)

if __name__ == "__main__":
    conn = sqlite3.connect("bank.db")
    initialize_database(conn)

    atm = ATM(conn)

    insert_sample_data(atm)

    print("🏧 Welcome to Python Bank ATM\n")
    atm.run()
