"""Module that cointains all bank and transaction related classes"""
from __future__ import annotations
from typing import TypeVar, Optional

from .transaction import Transaction

A = TypeVar("A", bound="Account")
B = TypeVar("B", bound="BankAccount")


class Account:
    """

    Attributes:
        balance:
        transactions:

    """

    def __init__(self: A) -> None:
        self.balance = 0
        self.transactions: list[Transaction] = []

    def check_positive(self: A, value: int) -> int:
        """

        Args:
            value (int):

        Returns:


        Raises:
            ValueError:

        """
        if value < 0:
            raise ValueError("Value cannot be negative")
        return value

    def get_balance(self: A) -> int:
        """

        Returns:


        """
        return self.balance

    def add_transaction_to_history(
        self: A, transaction_type: Transaction.TransactionType, amount: int
    ) -> Transaction:
        """

        Args:
            transaction_type (Transaction.TransactionType):
            amount (int):

        """
        trx = Transaction(transaction_type, amount, self.get_balance())
        self.transactions.append(trx)
        print(len(self.transactions))
        return trx

    def deposit(self: A, amount: int) -> None:
        """

        Args:
            amount (int):

        """
        self.check_positive(amount)
        self.balance += amount
        self.add_transaction_to_history(
            Transaction.TransactionTypes.DEPOSIT, amount
        )

    def withdraw(self: A, amount: int) -> Optional[Transaction]:
        """

        Args:
            amount (int):

        """
        trx = None
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

    def __init__(self: B, allow_overdraft: bool = False) -> None:
        super().__init__()
        self.allow_overdraft = allow_overdraft

    def is_overdrawn(self: B) -> bool:
        """

        Returns:


        """
        return self.balance < 0

    def withdraw(self: B, amount: int) -> Optional[Transaction]:
        """

        Args:
            amount (int):

        """
        trx = None
        self.check_positive(amount)
        if (self.balance - amount) < 0 and not self.allow_overdraft:
            print("Insufficient balance")
        else:
            self.balance -= amount
            trx = self.add_transaction_to_history(
                Transaction.TransactionTypes.WITHDRAWAL, amount
            )
        return trx
