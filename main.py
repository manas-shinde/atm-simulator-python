from atm.core.atm import ATM
from atm.models import User, Account

if __name__ == "__main__":
    atm = ATM()

    # Add sample admin
    admin = User("admin1", "Admin", "admin")
    admin.add_account(Account(9999, "0000", 10000))
    atm.add_user(admin)

    # Add sample user
    user = User("user1", "Alice")
    user.add_account(Account(1001, "1234", 5000))
    atm.add_user(user)

    print("🏧 Welcome to Python Bank ATM\n")
    atm.run()
