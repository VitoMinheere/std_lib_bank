from __future__ import annotations

from .transaction import Transaction


class Account:
    """

    Attributes:
        balance:
        transactions:

    """

    def __init__(self):
        self.balance = 100
        self.transactions = []

    def check_positive(self, value: int) -> int:
        """

        Args:
            value (int):

        Returns:


        Raises:
            ValueError:

        """
        if value < 0:
            raise ValueError("Value cannot be negative")
        else:
            return value

    def get_balance(self) -> int:
        return self.balance

    def add_transaction_to_history(
        self, transaction_type: Transaction.TransactionType, amount: int
    ):
        """

        Args:
            transaction_type (Transaction.TransactionType):
            amount (int):

        """
        trx = Transaction(transaction_type, amount, self.get_balance())
        self.transactions.append(trx)
        print(len(self.transactions))
        return trx

    def deposit(self, amount: int) -> None:
        """

        Args:
            amount (int):

        """
        self.check_positive(amount)
        self.balance += amount
        self.add_transaction_to_history(
            Transaction.TransactionTypes.DEPOSIT, amount
        )

    def withdraw(self, amount: int) -> Transaction:
        """

        Args:
            amount (int):

        """
        self.check_positive(amount)
        if (self.balance - amount) < 0:
            print("Insufficient balance")
        else:
            self.balance -= amount
            trx = self.add_transaction_to_history(
                Transaction.TransactionTypes.WITHDRAWAL, amount
            )
            return trx


class BankAccount(Account):
    """

    Attributes:
        allow_overdraft:

    """

    def __init__(self, allow_overdraft: bool = False):
        super(BankAccount, self).__init__()
        self.allow_overdraft = allow_overdraft

    def is_overdrawn(self) -> bool:
        """

        Returns:


        """
        return self.balance < 0

    def withdraw(self, amount: int) -> None:
        """

        Args:
            amount (int):

        """
        self.check_positive(amount)
        if (self.balance - amount) < 0 and not self.allow_overdraft:
            print("Insufficient balance")
        else:
            self.balance -= amount
            trx = self.add_transaction_to_history(
                Transaction.TransactionTypes.WITHDRAWAL, amount
            )
            return trx
