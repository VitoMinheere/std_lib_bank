"""Build the app"""
from app.classes.bank import BankAccount
from app.gui.bank import BankAccountUI

if __name__ == "__main__":
    account = BankAccount()
    BankAccountUI(account).create_ui()
