from __future__ import annotations

from enum import Enum


class Transaction:
    class TransactionTypes(Enum):
        DEPOSIT = 0
        WITHDRAWAL = 1

    def __init__(self, trx_type: TransactionTypes, amount: int):
        self.trx_type = trx_type
        self.amount = 0
