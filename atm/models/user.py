import sqlite3


class User:
    def __init(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_user(self, user_id: str, name: str, role: str = "user"):
        try:
            with self.conn:
                self.conn.execute(
                    "INSERT INTO users (user_id, name, role) VALUES (?, ?, ?)",
                    (user_id, name, role)
                )
            print(f"✅ User '{name}' (ID: {user_id}) with role '{role}' created.")
        except sqlite3.IntegrityError:
            print("❌ Error: User ID already exists.")

    # def add_account(self, account: Account):
    #     if account.account_number in self.accounts:
    #         raise ValueError(f"Account already exists for user - {self.name}")
    #     self.accounts[account.account_number] = account
    #
    # def get_account(self, acc_no: int):
    #     return self.accounts.get(acc_no)

    def get_user(self, user_id: str):
        cur = self.conn.cursor()
        cur.execute("SELECT user_id, name, role FROM users WHERE user_id = ?", (user_id,))
        return cur.fetchone()  # returns tuple or None

    def is_admin(self, user_id: str):
        user = self.get_user(user_id)
        return user and user[2] == 'admin'
