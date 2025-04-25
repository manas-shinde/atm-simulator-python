class Account:
    def __init__(self, account_number: int, name: str, login_pin: str, balance: float):
        self.account_number = account_number
        self.name = name
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
