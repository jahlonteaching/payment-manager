import random
import time

from app.errors import CreditCardError, TransferError, InsufficientFundsError
from app.payment import Payment, CreditCardPayment, BankTransferPayment, ElectronicWalletPayment


def process_payment_method(payment: Payment, amount: float):
    """
    Procesa un pago utilizando un método de pago específico.
    La función muestra mensajes del tipo INFO para indicar el estado del proceso de pago. Igualmente,
    se manejan los errores específicos de cada método de pago, para lo cual se capturan las excepciones
    CreditCardError, TransferError e InsufficientFundsError y se muestran mensajes de error personalizados
    del tipo Error.


    Args:
        payment (Payment): Método de pago a utilizar.
        amount (float): Monto a pagar.
    """
    payment_successful = False
    print(f"INFO: Iniciando proceso de pago - {type(payment).__name__}")
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
    # Se simula un proceso de pago con diferentes métodos de pago.
    # La instrucción del while con el operador := permite asignar el resultado de la comparación
    # en la variable continue_exec y evaluarla en la misma línea. Es una forma más compacta de
    # escribir el código.
    while continue_exec := input("¿Desea continuar? (s/n): ").lower() == "s":
        # Se genera una cuenta bancaria válida o invalida de forma aleatoria.
        bank_account = "BANK123" if random.randint(0, 1) else "INVALID"
        # Se crea una lista con los diferentes métodos de pago disponibles.
        payment_methods = [CreditCardPayment(1000), BankTransferPayment(bank_account), ElectronicWalletPayment()]
        # Se selecciona un monto aleatorio a pagar.
        amount_to_pay = random.randint(500, 1500)
        # Se selecciona un método de pago aleatorio y se invoca la función process_payment_method para procesar el pago.
        process_payment_method(random.choice(payment_methods), amount_to_pay)
