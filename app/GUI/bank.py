import tkinter as tk
from ..classes.bank import BankAccount


class BankAccountUI:
    def __init__(self, account: BankAccount):
        self.account = account

    def create_ui(self):
        # Creating a new window
        bank_acc = tk.Tk()
        bank_acc.geometry("600x300")
        bank_acc.title("Transfer Money")
        bank_acc.configure(bg="orange")

        # balance display
        self.account_balance = tk.IntVar()
        self.account_balance.set(self.account.get_balance())
        self.balance_entry = tk.Entry(
            bank_acc, textvariable=self.account_balance
        )
        self.balance_entry.pack(side="top")

        # deposit
        deposit_label = tk.Label(
            bank_acc, text="Deposit amount", relief="raised"
        )
        deposit_label.pack(side="top")

        deposit_amount = tk.IntVar()

        self.deposit_entry = tk.Entry(bank_acc, textvariable=deposit_amount)
        self.deposit_entry.pack(side="top")

        deposit_label = tk.Label(
            bank_acc, text="Enter Amount to be deposited", relief="raised"
        )
        deposit_label.pack(side="top")

        deposit_button = tk.Button(
            bank_acc, text="Submit", command=lambda: self.deposit()
        )
        deposit_button.pack(side="top")

        # withdraw
        withdraw_label = tk.Label(
            bank_acc, text="Withdrawl amount", relief="raised"
        )
        withdraw_label.pack(side="top")

        withdraw_amount = tk.IntVar()

        self.withdraw_entry = tk.Entry(bank_acc, textvariable=withdraw_amount)
        self.withdraw_entry.pack(side="top")

        withdraw_label = tk.Label(
            bank_acc, text="Enter Amount to be withdrawn", relief="raised"
        )
        withdraw_label.pack(side="top")

        withdraw_button = tk.Button(
            bank_acc, text="Withdraw", command=lambda: self.withdraw()
        )
        withdraw_button.pack(side="top")

        bank_acc.mainloop()

    def update(self):
        self.display_account_status()

    def deposit(self):
        self.account.deposit(int(self.deposit_entry.get()))
        self.account_balance.set(self.account.get_balance())
        self.update()

    def withdraw(self):
        self.account.withdraw(int(self.withdraw_entry.get()))
        self.account_balance.set(self.account.get_balance())
        self.update()

    def display_account_status(self):
        if self.account.is_overdrawn():
            self.balance_entry.config({"background": "Red"})
        else:
            self.balance_entry.config({"background": "Green"})
