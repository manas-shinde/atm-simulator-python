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
│   ├── atm.py          # ATM logic (login, deposit, withdraw, etc.)
│   ├── crypto_manager.py  # Handles encryption, decryption, file I/O
│
├── models/
│   ├── user.py         # User class (admin or user)
│   ├── account.py      # Account class (balance, PIN, etc.)
│
├── data/
│   ├── users.enc       # Encrypted users data (auto-created)
│   ├── accounts.enc    # Encrypted accounts data (auto-created)
│
├── main.py             # Entry point for running ATM
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
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
    - If no atm/data/ folder or encrypted files exist, they are created automatically.
    - Sample Admin and User are added for you.
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

## 📚 How Encryption Works

- When saving:
    - Data (Python dictionary) ➡️ Serialized ➡️ Encrypted ➡️ Saved as .enc file.
- When loading:
    - File ➡️ Decrypted ➡️ Deserialized ➡️ Python dictionary loaded in memory.

Encryption key is automatically generated/stored securely (can be extended for .env or vault-based storage).

---

## 🔥 Tech Stack

| Technology            | Purpose                     |
|-----------------------|-----------------------------|
| Python 3.x            | Programming Language        |
| cryptography (Fernet) | Data encryption             |
| OOP                   | Object-Oriented Programming |

---

## 💡 Future Enhancements
 - Password-based Key Derivation (PBKDF2) for better key management.

 - Backup encrypted data periodically.

---

## 👨‍💻 Author

    Developed by Manas, passionate about secure software development and smart solutions.
    (Designed to reflect a professional 3+ years experience level.)

--- 

## ⚡ Quick Demo

```commandline
🏧 Welcome to Python Bank ATM

🆔 Enter user ID: user1
🏦 Enter account number: 1001
🔒 Enter PIN: 1234

✅ Welcome, Alice!

📋 Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Logout
```