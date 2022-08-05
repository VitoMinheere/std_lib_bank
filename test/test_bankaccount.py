import unittest

from app.classes.bank import Account, BankAccount


class TestAccount(unittest.TestCase):
    def test_init(self):
        account = Account()
        self.assertEqual(account.balance, 0)

    def test_add_funds(self):
        account = Account()
        account.deposit(1000)
        self.assertEqual(account.balance, 1000)

    def test_add_negative_funds(self):
        account = Account()
        with self.assertRaises(ValueError):
            account.deposit(-1000)

    def test_withdraw_funds_overdraft(self):
        account = Account()
        account.deposit(100)
        account.withdraw(110)
        self.assertNotEqual(account.balance, -10)

    def test_add_transaction_to_history(self):
        account = Account()
        account.deposit(1000)
        self.assertGreater(len(account.transactions), 0)


class TestBankAccount(unittest.TestCase):
    def test_withdraw_funds(self):
        bank_account = BankAccount()
        bank_account.deposit(100)
        bank_account.withdraw(10)
        self.assertEqual(bank_account.balance, 90)

    def test_withdraw_funds_overdraft(self):
        bank_account = BankAccount()
        bank_account.deposit(100)
        bank_account.withdraw(110)
        self.assertNotEqual(bank_account.balance, -10)

    def test_withdraw_funds_allow_overdraft(self):
        bank_account = BankAccount(allow_overdraft=True)
        bank_account.deposit(100)
        bank_account.withdraw(110)
        self.assertEqual(bank_account.balance, -10)


if __name__ == "__main__":
    unittest.main()
