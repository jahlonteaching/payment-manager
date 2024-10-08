import random

from typing import Protocol

from app.errors import CreditCardError, TransferError, InsufficientFundsError


class Payment(Protocol):
    def process_payment(self, amount: float) -> bool:
        ...


class CreditCardPayment(Payment):

    def __init__(self, limit: float):
        self.limit: float = limit

    def process_payment(self, amount: float) -> bool:
        if amount > self.limit:
            raise CreditCardError("Credit card limit exceeded")

        print(f"Processing credit card payment for ${amount}")

        if random.randint(0, 10) > 7:
            return False

        return True


class BankTransferPayment(Payment):

    def __init__(self, account: str):
        self.account: str = account

    def _verify_account(self) -> bool:
        return self.account.startswith("BANK")

    def process_payment(self, amount: float) -> bool:
        if not self._verify_account():
            raise TransferError("Invalid bank account")

        print(f"Processing bank transfer payment for ${amount}")

        if random.randint(0, 10) > 8:
            return False

        return True


class ElectronicWalletPayment(Payment):

    def __init__(self):
        self.balance: float = random.randint(1000, 10000)

    def process_payment(self, amount: float) -> bool:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")

        print(f"Processing electronic wallet payment for ${amount}")

        if random.randint(0, 10) > 9:
            return False

        return True

