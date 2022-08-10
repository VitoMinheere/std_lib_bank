"""Module to handle Transaction"""
from __future__ import annotations

from enum import Enum
from typing import Dict, TypeVar

T = TypeVar("T", bound="Transaction")


class Transaction:
    """

    Attributes:
        amount:
        trx_type:
        account_value:

    """

    class TransactionTypes(Enum):
        """Hold all transaction types"""

        DEPOSIT = 0
        WITHDRAWAL = 1

    def __init__(
        self: T, trx_type: TransactionTypes, amount: int, account_value: int
    ) -> None:
        self.trx_type = trx_type
        self.amount = amount
        self.account_value = account_value

    def serialize(self: T) -> Dict:
        """

        Returns:


        """
        serialized = {
            "type": self.trx_type.name.capitalize(),
            "amount": self.amount,
            "balance": self.account_value,
        }
        return serialized
