""" Build the main UI"""
import tkinter as tk
from typing import TypeVar

from ..classes.bank import BankAccount
from .bank import BankAccountUI

S = TypeVar("S", bound="Screen")


class Screen:
    """

    Attributes:
        root:

    """

    def __init__(self: S) -> None:
        self.root = tk.Tk()
        self.root["title"] = "Bank app"
        self.root.configure(bg="lightgray")

    def create_bank_account_screen(self: S, account: BankAccount) -> None:
        """

        Args:
            account (BankAccount):

        """
        BankAccountUI(account).create_ui()
