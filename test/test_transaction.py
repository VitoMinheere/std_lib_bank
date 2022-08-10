import unittest
from typing import Dict

from app.classes.transaction import Transaction


class TestBankTransaction(unittest.TestCase):
    def test_create_transaction(self):
        trx = Transaction(Transaction.TransactionTypes.DEPOSIT, 100, 100)
        self.assertIs(trx.trx_type, Transaction.TransactionTypes.DEPOSIT)

    def test_serialize(self):
        trx = Transaction(Transaction.TransactionTypes.DEPOSIT, 100, 100)
        serialized = trx.serialize()
        self.assertIsInstance(serialized, Dict)
        self.assertListEqual(list(serialized.keys()), ["type", "amount", "balance"])

