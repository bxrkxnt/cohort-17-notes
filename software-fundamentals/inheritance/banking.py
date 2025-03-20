"""Implementation of bank acount classes."""

from datetime import datetime
from uuid import uuid4

class Transaction:

    def __init__(self, transaction_type: str, amount=None):
        self.transaction_type = transaction_type
        self.amount = amount
        self.at = datetime.now()


class BankAccount:
    """A simple bank account."""
    
    def __init__(self, initial_balance):
        self.account_id = uuid4()
        self._balance = initial_balance
        self.transactions = [Transaction("ACCOUNT CREATED")]

    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, amount) -> None:
        if self._balance + amount > 0:
            self._balance += amount
        else:
            raise ValueError("Balance cannot go below zero!")
    
    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount!")
        self.balance = -amount
        self.transactions.append(Transaction("WITHDRAW", -amount))

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount!")
        self.balance = amount
        self.transactions.append(Transaction("DEPOSIT", amount))
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.account_id} ({self.balance})"

    def __str__(self) -> str:
        return self.__repr__()


class InterestAccount(BankAccount):

    def __init__(self, initial_balance, interest_rate):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def collect_interest(self) -> None:
        amount = self._balance * self.interest_rate
        self.deposit(amount)


class TaxFreeInterestAccount(InterestAccount):
    
    def __init__(self, initial_balance, interest_rate):
        super().__init__(initial_balance, interest_rate)
    
    def deposit(self, amount: float) -> None:
       super().deposit(amount * 1.2)


if __name__ == "__main__":
    tf = TaxFreeInterestAccount(100, 0.5)
    tf.deposit(100)
    print(tf)