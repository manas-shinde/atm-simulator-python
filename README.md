# 🏧 Python Bank ATM — Encrypted File Storage Version

Welcome to **Python Bank ATM**, a simulation of a real ATM system where user and account data are securely stored **with
encryption** in local files.

This version uses **Fernet encryption** (from `cryptography` library) to ensure all sensitive data like PINs, balances,
and user details are protected even at the file system level.

---

## ✨ Features

- Create **Admin** and **User** accounts.
- **Login** securely using account number and PIN.
- **Deposit**, **Withdraw**, **Check Balance**, **Change PIN**.
- **Admin** can add new users and view existing users.
- All data (users, accounts) are **encrypted** and stored in `atm/data/` directory.
- **Auto save and load** system state at startup and shutdown.

---

## 🔐 Security

- All saved user/account data is **encrypted** using **Fernet symmetric encryption**.
- PINs are securely **hashed** before storage.
- Even if files are stolen, without the encryption key they are unreadable.

---

## 🛠 Project Structure

```commandline
atm/ 
│ 
├── core/ 
│ 
├── atm.py # ATM logic (login, deposit, withdraw, etc.) 
│ 
├── database_manager.py # Handles SQLite3 database operations 
│ 
├── models/ 
│ 
├── user.py # User class (admin or user) 
│ 
├── account.py # Account class (balance, PIN, etc.) 
│ 
├── data/ 
│ 
└── atm.db # SQLite3 database file (auto-created) 
│ 
├── main.py # Entry point for running ATM 
├── README.md # Project documentation 
└── requirements.txt # Python dependencies
```

---

## 📦 Setup Instructions

1. **Install Python packages:**
    ```bash
   pip install cryptography
   ```
2. Run the application:
    ```bash
    python main.py
    ```
3. First Time Run:
    - If the database atm/data/atm.db does not exist, it will be created automatically with required tables.
    - Sample Admin and User accounts are inserted for you.
4. Default Credentials (for testing):

```
   Admin:

       User ID: admin1
   
       Account Number: 9999
   
       PIN: 0000
   
   User:
   
       User ID: user1
   
       Account Number: 1001
   
       PIN: 1234
   ```

---

## 🗄️ How Data is Stored

- SQLite database stores:

    - Users Table → user_id, name, role.

    - Accounts Table → account_number, PIN (hashed), balance, user_id (foreign key).

- Secure hashing of PINs before saving into the database.

- All operations like login, deposit, withdraw, and PIN change directly reflect into the database.

---

## 💡 Future Enhancements

- Add transaction history (passbook).

- Apply password-based encryption on the database file.

---

## 👨‍💻 Author

- Developed by Manas, focused on building robust backend systems and smart automation solutions.
  (Optimized for real-world, small-to-medium scale banking simulations.)