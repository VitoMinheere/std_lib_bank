import unittest

from app.classes.bank import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_init(self):
        bank_account = BankAccount()
        self.assertEqual(bank_account.balance, 0)

    def test_add_funds(self):
        bank_account = BankAccount()
        bank_account.deposit(1000)
        self.assertEqual(bank_account.balance, 1000)

    def test_add_negative_funds(self):
        bank_account = BankAccount()
        with self.assertRaises(ValueError):
            bank_account.deposit(-1000)

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
