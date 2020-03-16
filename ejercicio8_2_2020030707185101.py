"""
Ejercicio 8: Pedirle al usuario que ingrese por teclado 3 números
binarios de 8 bits, para cada uno imprimir su siguiente (número + 1)
pero en sistema decimal. Recuerden que los números binarios están compuestos por 1 y 0.
"""
binarios = []

for i in range(3):
    binario = input("Ingrese el número en formato binario: ")
    binarios.append(binario)

decimal = 0

for binario in binarios:
    binario = binario[::-1]
    for i in range(len(binario)):
        decimal += int(binario[i]) * (2**i)
    print(decimal + 1)
    decimal = 0











