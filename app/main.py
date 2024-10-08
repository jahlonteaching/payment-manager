import random
import time

from app.errors import CreditCardError, TransferError, InsufficientFundsError
from app.payment import Payment, CreditCardPayment, BankTransferPayment, ElectronicWalletPayment


def process_payment_method(payment: Payment, amount: float):
    payment_successful = False
    print("INFO: Iniciando proceso de pago.")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print()
    try:
        payment_successful = payment.process_payment(amount)
    except CreditCardError:
        print("Error: El monto excede el límite permitido para pagos con tarjeta de crédito.")
    except TransferError:
        print("Error: Número de cuenta inválido para la transferencia bancaria.")
    except InsufficientFundsError:
        print("Error: Fondos insuficientes en el monedero electrónico.")
    else:
        if not payment_successful:
            print("INFO: El pago no pudo ser procesado.")
        else:
            print("INFO: Pago procesado exitosamente.")
    finally:
        print("INFO: Proceso de pago finalizado.")


if __name__ == "__main__":
    bank_account = "BANK123" if random.randint(0, 1) else "INVALID"
    payment_methods = [CreditCardPayment(1000), BankTransferPayment(bank_account), ElectronicWalletPayment()]
    amount_to_pay = random.randint(500, 1500)
    process_payment_method(random.choice(payment_methods), amount_to_pay)
