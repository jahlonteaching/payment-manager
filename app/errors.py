class PaymentManagerError(Exception):
    """Clase base para excepciones en el módulo payment-manager."""
    pass


class CreditCardError(PaymentManagerError):
    """
    Excepción lanzada para errores en la tarjeta de crédito.
    """
    pass


class TransferError(PaymentManagerError):
    """
    Excepción lanzada para errores en la transferencia bancaria.
    """
    pass


class InsufficientFundsError(PaymentManagerError):
    """
    Excepción lanzada para errores de fondos insuficientes.
    """
    pass