class Account:
    def __init__(self, account_number: int, login_pin: str, balance: float = 1000.0):
        self.account_number = account_number
        self.__pin = login_pin
        self.balance = balance

    def deposit(self, amt: float):
        self.balance += amt
        print(f"After adding amount {amt} to account, current balance is {self.balance}")

    def withdraw(self, amt: float):
        if amt > self.balance or self.balance - amt < 0:
            print(f"Insufficient balance!!")
        else:
            self.balance -= amt
            print(f"Withdraw RS.{amt}. Current balance is {self.balance}")

    def change_pin(self, old_pin: str, new_pin: str):
        if new_pin == self.__pin:
            print(f"New pin can't be similar to existing pin.")
        elif old_pin == self.__pin and new_pin != self.__pin:
            self.__pin = new_pin
            print(f"Login Pin updated successfully.")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def check_pin(self, pin: str):
        return pin == self.__pin

    def __str__(self):
        return f"{self.account_number} - {self.balance}"

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'pin': self.__pin,
            'balance': self.balance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['account_number'], data['pin'], data['balance'])
