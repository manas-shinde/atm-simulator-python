CREATE TABLE IF NOT EXISTS users(
user_id TEXT PRIMARY NOT NULL,
name TEXT NOT NULL,
role TEXT Check(role IN ('admin','user')) NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts(
account_no TEXT PRIMARY NOT NULL,
balance FLOAT NOT NULL,
pin TEXT NOT NULL,
user_id TEXT,
FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS transactions (
    txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT NOT NULL,
    action TEXT NOT NULL,
    amount REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
);
