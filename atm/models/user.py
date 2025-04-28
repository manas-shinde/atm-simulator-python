from atm.models.account import Account


class User:
    def __init__(self, user_id: str, name: str, role: str = "user"):
        self.user_id = user_id
        self.name = name
        self.role = role  # 'admin' or 'user'
        self.accounts = {}  # account_number -> Account

    def add_account(self, account: Account):
        if account.account_number in self.accounts:
            raise ValueError(f"Account already exists for user - {self.name}")
        self.accounts[account.account_number] = account

    def get_account(self, acc_no: int):
        return self.accounts.get(acc_no)

    def is_admin(self):
        return self.role == "admin"

    def __str__(self):
        return f"{self.user_id} - {self.name}"

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'accounts': {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data['user_id'], data['name'], data['role'])
        for acc_no, acc_data in data["accounts"].items():
            user.add_account(Account.from_dict(acc_data))

        return user
