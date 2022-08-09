import tkinter as tk

from bank import BankAccountUI


class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = "Bank app"
        self.root.configure(bg="lightgray")

    def create_bank_account_screen(self, account):
        BankAccountUI(account).create_ui()
