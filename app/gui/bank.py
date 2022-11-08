"""Build bank account UI for deposit and withdraw"""
import tkinter as tk
from tkinter import ttk
from typing import TypeVar

from ..classes.bank import BankAccount, Transaction

BUI = TypeVar("BUI", bound="BankAccountUI")
TH = TypeVar("TH", bound="TransactionHistory")


class BankAccountUI:
    """

    Attributes:
        withdraw_entry:
        bank_acc:
        balance_entry:
        account_balance:
        upper_frame:
        account:
        trx_list:
        middle_frame:
        deposit_entry:
        deposit:
        withdraw:
        root:

    """

    def __init__(self: BUI, account: BankAccount) -> None:
        self.account = account
        self.root = tk.Tk()
        self.bank_acc = tk.Frame(self.root)
        self.upper_frame = tk.Frame(self.bank_acc)
        self.middle_frame = tk.Frame(self.bank_acc)
        self.balance_entry = tk.Entry()
        self.deposit_entry = tk.Entry()
        self.withdraw_entry = tk.Entry()
        self.account_balance = tk.IntVar()
        self.trx_list = TransactionHistory(self.root)

    def create_ui(self: BUI) -> None:
        """ """
        self.create_root()
        self.create_window()
        self.create_upper_frame()
        self.create_balance_display()
        self.create_middle_frame()
        self.create_deposit_view()
        self.create_withdrawal_view()

        self.add_transaction_list()

        self.root.mainloop()

    def create_root(self: BUI) -> None:
        """ """
        root = tk.Tk()
        root.geometry("900x600")
        root.title("Transfer Money")
        root.configure(bg="orange")
        self.root = root

    def create_window(self: BUI) -> None:
        """ """
        bank_acc = tk.Frame(self.root)
        bank_acc.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.bank_acc = bank_acc

    def create_upper_frame(self: BUI) -> None:
        """ """
        frame = tk.Frame(self.bank_acc, bg="#80c1ff")
        frame.place(relx=0.4, rely=0.1)
        self.upper_frame = frame

    def create_balance_display(self: BUI) -> None:
        """ """
        balance_label = tk.Label(self.upper_frame, text="Account balance")
        balance_label.pack(side="left")

        self.account_balance = tk.IntVar()
        self.account_balance.set(self.account.get_balance())
        self.balance_entry = tk.Entry(
            self.upper_frame, textvariable=self.account_balance
        )
        self.balance_entry.pack(side="right")

    def create_middle_frame(self: BUI) -> None:
        """ """
        frame = tk.Frame(self.bank_acc, bg="#80c1ff")
        frame.place(relx=0.4, rely=0.4)
        self.middle_frame = frame

    def create_deposit_view(self: BUI) -> None:
        """ """
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

        deposit_button = tk.Button(
            self.middle_frame, text="Submit", command=self.deposit
        )
        deposit_button.pack(side="top")

    def create_withdrawal_view(self: BUI) -> None:
        """ """
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

        withdraw_button = tk.Button(
            self.middle_frame, text="Withdraw", command=self.withdraw
        )
        withdraw_button.pack(side="top")

    def add_transaction_list(self: BUI) -> None:
        """ """
        self.trx_list.create_transaction_list()

    def update(self: BUI) -> None:
        """ """
        # self.account_balance.set(self.account.get_balance())
        self.display_account_status()

    def deposit(self: BUI) -> None:
        """ """
        trx = self.account.deposit(int(self.deposit_entry.get()))
        if trx:
            self.trx_list.add_to_list(trx)
        self.update()

    def withdraw(self: BUI) -> None:
        """ """
        trx = self.account.withdraw(int(self.withdraw_entry.get()))
        if trx:
            self.trx_list.add_to_list(trx)
        self.update()

    def display_account_status(self: BUI) -> None:
        """ """
        if self.account.is_overdrawn():
            self.balance_entry.config({"background": "Red"})
        else:
            self.balance_entry.config({"background": "Green"})


class TransactionHistory:
    """
    Widget to display transaction history in a list
    """

    def __init__(self: TH, frame: tk.Tk) -> None:
        self.frame = frame
        self.trx_tree = ttk.Treeview(self.frame)
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)

    def create_transaction_list(self: TH) -> None:
        """
        Create table to display transaction history

        """
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

        # self.trx_tree.insert(
        #     parent="", index="end", values=["Deposit", "12", "12"]
        # )
        self.trx_tree.pack(pady=2)

    def add_to_list(self: TH, trx: Transaction) -> None:
        """

        Args:
            trx (Transaction):

        """
        self.trx_tree.insert(
            parent="", index="end", values=list(trx.serialize().values())
        )
