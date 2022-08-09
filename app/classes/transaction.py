from __future__ import annotations

from enum import Enum


class Transaction:
    class TransactionTypes(Enum):
        DEPOSIT = 0
        WITHDRAWAL = 1

    def __init__(
        self, trx_type: TransactionTypes, amount: int, account_value: int
    ):
        self.trx_type = trx_type
        self.amount = amount
        self.account_value = account_value

    def serialize(self):
        serialized = {
            "type": self.trx_type.name.capitalize(),
            "amount": self.amount,
            "balance": self.account_value,
        }
        return serialized
