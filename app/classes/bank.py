class BankAccount:
    def __init__(self, allow_overdraft: bool = False):
        self.balance = 0
        self.allow_overdraft = allow_overdraft

    def check_positive(self, value: int) -> int:
        if value < 0:
            raise ValueError("Value cannot be negative")
        else:
            return value

    def get_balance(self) -> int:
        return self.balance

    def is_overdrawn(self) -> bool:
        return self.balance < 0

    def deposit(self, amount: int) -> None:
        self.check_positive(amount)
        self.balance += amount
        print(self.get_balance())

    def withdraw(self, amount: int) -> None:
        self.check_positive(amount)
        if (self.balance - amount) < 0 \
                and not self.allow_overdraft:
            print("Insufficient balance")
        else:
            self.balance -= amount
