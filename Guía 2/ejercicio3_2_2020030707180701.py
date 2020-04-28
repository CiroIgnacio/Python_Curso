"""
Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números, si el primero es menor que el segundo imprimir la
resta entre el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos, y si son iguales imprimir su producto.
"""
try:
    num1 = float(input("Ingrese un número: "))
    num2 = float(input("Ingrese un número: "))
    if num1 < num2:
        operacion = num2 - num1
    elif num1 > num2:
        operacion = num1 + num2
    else:
        operacion = num1 * num2

    print(operacion)

except ValueError:
    print("Debe ingresar sólo números")