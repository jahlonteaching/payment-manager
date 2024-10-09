# Ejercicio: Sistema de Gestión de Pagos

## Descripción
En este ejercicio, se te solicita implementar un sistema de gestión de pagos para una tienda en línea. La tienda acepta diferentes métodos de pago, como **tarjetas de crédito**, **transferencias bancarias** y **monederos electrónicos**. Cada método de pago tiene su propia lógica de procesamiento, y el sistema debe ser capaz de gestionar cualquier error que ocurra durante el proceso de pago.

Utilizarás **abstracción** mediante el uso de **protocolos** para definir una interfaz común que todos los métodos de pago deben seguir. Además, deberás implementar un manejo adecuado de excepciones para gestionar posibles errores en el proceso de pago.

## Requisitos

1. **Protocolo `Pago`:**
   - Define un protocolo llamado `Pago` que incluya el método abstracto:
     - `procesar_pago(monto: float) -> bool`: Método que debe implementar la lógica para procesar el pago y devolver `True` si el pago es exitoso o `False` en caso contrario.
   - Los métodos definidos en el protocolo no deben tener una implementación concreta, ya que esta será responsabilidad de las clases que implementen el protocolo.

2. **Implementación de métodos de pago:**
   - Crea tres clases que representen diferentes métodos de pago, cada una implementando el protocolo `Pago`:
     - **TarjetaCredito:** Esta clase debe simular el proceso de pago con tarjeta de crédito. Si el monto es superior a un límite (por ejemplo, 5000), debe lanzar una excepción personalizada `TarjetaCreditoError`.
     - **TransferenciaBancaria:** Esta clase debe manejar las transferencias bancarias. Si hay un error en el número de cuenta, debe lanzar una excepción personalizada `TransferenciaError`.
     - **MonederoElectronico:** Esta clase simula el uso de un monedero electrónico. Si el saldo del monedero es insuficiente, debe lanzar una excepción `SaldoInsuficienteError`.

3. **Manejo de excepciones:**
   - Crea las excepciones personalizadas necesarias (`TarjetaCreditoError`, `TransferenciaError`, `SaldoInsuficienteError`) para gestionar los diferentes errores que pueden ocurrir durante el proceso de pago.
   - Implementa un manejo adecuado de excepciones que capture estos errores y muestre un mensaje claro para el usuario cuando el pago falle.

## Tareas

1. **Definir el protocolo `Pago`:**
   - Usa el módulo `typing` para definir un protocolo que contenga el método `procesar_pago`.

2. **Implementar clases de métodos de pago:**
   - Crea las clases `TarjetaCredito`, `TransferenciaBancaria` y `MonederoElectronico` que implementen el protocolo `Pago`.
   - Cada clase debe implementar el método `procesar_pago` y lanzar las excepciones correspondientes cuando ocurra un error.

3. **Probar el sistema de pagos:**
   - Escribe una función que reciba un objeto de tipo `Pago` y un monto, intente procesar el pago y maneje cualquier excepción que se produzca, mostrando un mensaje de error adecuado.

## Ejemplo de salida esperada

Si se intenta realizar un pago con una tarjeta de crédito con un monto superior al límite, el sistema debería capturar la excepción y mostrar un mensaje similar a:

`Error: El monto excede el límite permitido para pagos con tarjeta de crédito.`

Si se intenta realizar una transferencia bancaria con un número de cuenta inválido:

`Error: Número de cuenta inválido para la transferencia bancaria.`

Si se utiliza un monedero electrónico con saldo insuficiente:

`Error: Saldo insuficiente en el monedero electrónico.`