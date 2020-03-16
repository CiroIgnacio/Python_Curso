"""Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito.
Evaluar si puede realizar una compra de $2500, si puede indicar cuánto saldo le queda luego de efectuarla.
Si no puede, indicar cuánto dinero le falta para poder realizarla."""

montoDisp = int(input("Ingrese el monto disponible de su tarjeta de crédito: "))

if montoDisp >= 2500:
    nuevoMonto = montoDisp - 2500
    print(f"Su saldo actual es de ${nuevoMonto} pesos")
else:
    faltante = 2500 - montoDisp
    print(f"Le faltan ${faltante} pesos para poder realizar la compra")
