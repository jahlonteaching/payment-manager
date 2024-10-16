import random

from typing import Protocol

from app.errors import CreditCardError, TransferError, InsufficientFundsError


class Payment(Protocol):
    """
    Protocolo para definir el comportamiento de un pago.
    """
    def process_payment(self, amount: float) -> bool:
        """
        Procesa un pago.

        Args:
            amount (float): Monto a pagar.

        Returns:
            bool: True si el pago fue exitoso, False en caso contrario.
        """
        ...


class CreditCardPayment(Payment):
    """
    Clase que representa un pago con tarjeta de crédito.

    Attributes:
        limit (float): Límite de la tarjeta de crédito.
    """

    def __init__(self, limit: float):
        self.limit: float = limit

    def process_payment(self, amount: float) -> bool:
        """
        Implementación del método process_payment para un pago con tarjeta de crédito.
        El método simula el procesamiento de un pago con tarjeta de crédito, generando un resultado aleatorio
        donde el 70% de las veces el pago es exitoso.

        Args:
            amount (float): Monto a pagar.

        Returns:
            bool: True si el pago fue exitoso, False en caso contrario.

        Raises:
            CreditCardError: Si el monto a pagar excede el límite de la tarjeta de crédito.
        """
        if amount > self.limit:
            raise CreditCardError("Credit card limit exceeded")

        print(f"Processing credit card payment for ${amount}")

        if random.randint(0, 10) > 7:
            return False

        return True


class BankTransferPayment(Payment):
    """
    Clase que representa un pago con transferencia bancaria.

    Attributes:
        account (str): Número de cuenta bancaria.
    """
    def __init__(self, account: str):
        self.account: str = account

    def _verify_account(self) -> bool:
        """
        Verifica si la cuenta bancaria es válida. Para este ejemplo, se considera que una cuenta bancaria válida
        es aquella que comienza con la palabra "BANK".

        Returns:
        """
        return self.account.startswith("BANK")

    def process_payment(self, amount: float) -> bool:
        """
        Implementación del método process_payment para un pago con transferencia bancaria.
        El método simula el procesamiento de un pago con transferencia bancaria, generando un resultado aleatorio
        donde el 80% de las veces el pago es exitoso.

        Args:
            amount (float): Monto a pagar.

        Returns:
            bool: True si el pago fue exitoso, False en caso contrario.

        Raises:
            TransferError: Si la cuenta bancaria no es válida.
        """
        if not self._verify_account():
            raise TransferError("Invalid bank account")

        print(f"Processing bank transfer payment for ${amount}")

        if random.randint(0, 10) > 8:
            return False

        return True


class ElectronicWalletPayment(Payment):
    """
    Clase que representa un pago con billetera electrónica.

    Attributes:
        balance (float): Saldo de la billetera electrónica. Se inicializa con un valor aleatorio entre 1000 y 10000.
    """
    def __init__(self):
        self.balance: float = random.randint(1000, 10000)

    def process_payment(self, amount: float) -> bool:
        """
        Implementación del método process_payment para un pago con billetera electrónica.
        El método simula el procesamiento de un pago con billetera electrónica, generando un resultado aleatorio
        donde el 90% de las veces el pago es exitoso.

        Args:
            amount (float): Monto a pagar.

        Returns:
            bool: True si el pago fue exitoso, False en caso contrario.

        Raises:
            InsufficientFundsError: Si el monto a pagar excede el saldo de la billetera electrónica.
        """
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")

        print(f"Processing electronic wallet payment for ${amount}")

        if random.randint(0, 10) > 9:
            return False

        return True

