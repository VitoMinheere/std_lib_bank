import unittest

from app.classes.transaction import Transaction


class TestBankTransaction(unittest.TestCase):
    def test_create_transaction(self):
        trx = Transaction(Transaction.TransactionTypes.DEPOSIT, 100)
        self.assertIs(trx.trx_type, Transaction.TransactionTypes.DEPOSIT)
