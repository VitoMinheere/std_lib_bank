import tkinter as tk
from tkinter import ttk

from ..classes.bank import BankAccount, Transaction


class BankAccountUI:
    def __init__(self, account: BankAccount):
        self.account = account

    def create_ui(self):
        self.create_root()
        self.create_window()
        self.create_upper_frame()
        self.create_balance_display()
        self.create_middle_frame()
        self.create_deposit_view()
        self.create_withdrawal_view()

        self.trx_list = TransactionHistory(self.root)
        self.add_transaction_list()

        self.root.mainloop()

    def create_root(self):
        root = tk.Tk()
        root.geometry("600x300")
        root.title("Transfer Money")
        root.configure(bg="orange")
        self.root = root

    def create_window(self):
        # Creating a new window
        bank_acc = tk.Frame(self.root)
        bank_acc.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.bank_acc = bank_acc

    def create_upper_frame(self):
        frame = tk.Frame(self.bank_acc, bg="#80c1ff")
        frame.place(relx=0.4, rely=0.1)
        self.upper_frame = frame

    def create_balance_display(self):
        balance_label = tk.Label(self.upper_frame, text="Account balance")
        balance_label.pack(side="left")

        self.account_balance = tk.IntVar()
        self.account_balance.set(self.account.get_balance())
        self.balance_entry = tk.Entry(
            self.upper_frame, textvariable=self.account_balance
        )
        self.balance_entry.pack(side="right")

    def create_middle_frame(self):
        frame = tk.Frame(self.bank_acc, bg="#80c1ff")
        frame.place(relx=0.4, rely=0.4)
        self.middle_frame = frame

    def create_deposit_view(self):
        # deposit
        deposit_label = tk.Label(
            self.middle_frame, text="Deposit amount", relief="raised"
        )
        deposit_label.pack(side="top")

        deposit_amount = tk.IntVar()

        self.deposit_entry = tk.Entry(
            self.middle_frame, textvariable=deposit_amount
        )
        self.deposit_entry.place(relx=0.2, rely=0.8)
        self.deposit_entry.pack(side="top")

        # deposit_label = tk.Label(
        #     self.middle_frame, text="Enter Amount to be deposited", relief="raised"
        # )
        # deposit_label.pack(side="left")

        deposit_button = tk.Button(
            self.middle_frame, text="Submit", command=lambda: self.deposit()
        )
        deposit_button.pack(side="top")

    def create_withdrawal_view(self):
        # withdraw
        withdraw_label = tk.Label(
            self.middle_frame, text="Withdrawl amount", relief="raised"
        )
        withdraw_label.pack(side="top")

        withdraw_amount = tk.IntVar()

        self.withdraw_entry = tk.Entry(
            self.middle_frame, textvariable=withdraw_amount
        )
        self.withdraw_entry.place(relx=0.6, rely=0.4)
        self.withdraw_entry.pack(side="top")

        # withdraw_label = tk.Label(
        #     self.middle_frame, text="Enter Amount to be withdrawn", relief="raised"
        # )
        # withdraw_label.pack(side="top")

        withdraw_button = tk.Button(
            self.middle_frame, text="Withdraw", command=lambda: self.withdraw()
        )
        withdraw_button.pack(side="top")

    def add_transaction_list(self):
        self.trx_list.create_transaction_list()

    def update(self):
        self.account_balance.set(self.account.get_balance())
        self.display_account_status()

    def deposit(self):
        self.account.deposit(int(self.deposit_entry.get()))
        self.update()

    def withdraw(self):
        trx = self.account.withdraw(int(self.withdraw_entry.get()))
        if trx:
            self.trx_list.add_to_list(trx)
        self.update()

    def display_account_status(self):
        if self.account.is_overdrawn():
            self.balance_entry.config({"background": "Red"})
        else:
            self.balance_entry.config({"background": "Green"})


class TransactionHistory:
    """
    Widget to display transaction history in a list
    """

    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.trx_tree = ttk.Treeview(self.frame)

    def create_transaction_list(self):
        list_header_label = tk.Label(self.frame, text="Transaction history")
        list_header_label.pack(side="bottom")

        self.trx_tree["columns"] = ("Type", "Amount", "Balance")
        self.trx_tree.column("#0", width=0, stretch="n")
        self.trx_tree.column("Type", anchor="w", width=120)
        self.trx_tree.column("Amount", anchor="w", width=120)
        self.trx_tree.column("Balance", anchor="w", width=120)

        self.trx_tree.heading("Type", text="Type", anchor="w")
        self.trx_tree.heading("Amount", text="Amount", anchor="w")
        self.trx_tree.heading("Balance", text="Balance", anchor="w")

        self.trx_tree.insert(
            parent="", index="end", values=["Deposit", "12", "12"]
        )
        self.trx_tree.pack(pady=0)

    def add_to_list(self, trx: Transaction):
        self.trx_tree.insert(
            parent="", index="end", values=list(trx.serialize().values())
        )
