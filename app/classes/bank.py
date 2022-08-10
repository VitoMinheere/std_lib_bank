"""Module that cointains all bank and transaction related classes"""
from __future__ import annotations

from typing import TypeVar

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
        Return balance of an account
        """
        return self.balance

    def add_transaction_to_history(
        self: A, transaction_type: Transaction.TransactionType, amount: int
    ) -> Transaction:
        """
        Creates a Transactionobject and adds it to the trasnactions

        Args:
            transaction_type (Transaction.TransactionType):
            amount (int):

        """
        trx = Transaction(transaction_type, amount, self.get_balance())
        self.transactions.append(trx)
        return trx

    def deposit(self: A, amount: int) -> None:
        """
        Add funds to a bank account

        Args:
            amount (int): amount of funds to add

        """
        self.check_positive(amount)
        self.balance += amount
        self.add_transaction_to_history(
            Transaction.TransactionTypes.DEPOSIT, amount
        )

    def withdraw(self: A, amount: int) -> Transaction:
        """
        Retrieve money from account

        Args:
            amount (int): Amount of money to retrieve

        Raises:
            ValueError: If funds are not enough to cover the amount
        """
        self.check_positive(amount)
        if (self.balance - amount) < 0:
            raise ValueError("Insufficient balance")
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

    def withdraw(self: B, amount: int) -> Transaction:
        """
        Retrieve money from bank account.
        Balance can go into negavtive if allow_overdraft is true

        Args:
            amount (int):

        Returns:
            Transaction

        Raises:
            ValueError: If not enough balance and allow_overdraft is false

        """
        self.check_positive(amount)
        if (self.balance - amount) < 0 and not self.allow_overdraft:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        trx = self.add_transaction_to_history(
            Transaction.TransactionTypes.WITHDRAWAL, amount
        )
        return trx
