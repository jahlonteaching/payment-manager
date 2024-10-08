class PaymentManagerError(Exception):
    """Base class for exceptions in this module."""
    pass


class CreditCardError(PaymentManagerError):
    """Exception raised for errors in the credit card number.

    Attributes:
        message -- explanation of the error
    """


class TransferError(PaymentManagerError):
    """Exception raised for errors in the bank transfer.

    Attributes:
        message -- explanation of the error
    """


class InsufficientFundsError(PaymentManagerError):
    """Exception raised for errors in the insufficient funds.

    Attributes:
        message -- explanation of the error
    """