from __future__ import annotations

from .transaction import Transaction


class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def check_positive(self, value: int) -> int:
        if value < 0:
            raise ValueError("Value cannot be negative")
        else:
            return value

    def get_balance(self) -> int:
        return self.balance

    def add_transaction_to_history(
        self, transaction_type: Transaction.TransactionType, amount: int
    ):
        trx = Transaction(transaction_type, amount)
        self.transactions.append(trx)

    def deposit(self, amount: int) -> None:
        self.check_positive(amount)
        self.balance += amount
        self.add_transaction_to_history(
            Transaction.TransactionTypes.DEPOSIT, amount
        )

    def withdraw(self, amount: int) -> None:
        self.check_positive(amount)
        if (self.balance - amount) < 0:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.add_transaction_to_history(
                Transaction.TransactionTypes.WITHDRAWAL, amount
            )


class BankAccount(Account):
    def __init__(self, allow_overdraft: bool = False):
        super(BankAccount, self).__init__()
        self.allow_overdraft = allow_overdraft

    def is_overdrawn(self) -> bool:
        return self.balance < 0

    def withdraw(self, amount: int) -> None:
        self.check_positive(amount)
        if (self.balance - amount) < 0 and not self.allow_overdraft:
            print("Insufficient balance")
        else:
            self.balance -= amount
