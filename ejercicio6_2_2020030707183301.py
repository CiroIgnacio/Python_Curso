"""Ejercicio 6: Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles, una vez seleccionada la operación, introducir dos números y ejecutar la operación"""
print("Seleccione una operacion:\n1 - Suma\n2 - Resta\n3 - Multiplicacion\n4 - Division")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b, b - a

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if a != 0 and b != 0:
        return a / b, b / a
    else:
        if a == 0 and b != 0:
            return a / b, None
        if b == 0 and a != 0:
            return b / a, None
        if a == 0 and b == 0:
            return None, None
            print("Dividir por 0 no es valido")


operacion = input("Operación elegida: ")
try:
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
except ValueError:
    print("Solo se permite operar con numeros")

if operacion == '1':
    sum = suma(num1, num2)
    print(f"{num2} + {num1} = {sum}")


elif operacion == '2':
    res, res1 = resta(num1, num2)
    print(f"{num1} - {num2} = {res}\n{num2} - {num1} = {res1}")

elif operacion == '3':
    mult = multiplicacion(num1, num2)
    print(f"{num1} * {num2} = {mult}")

elif operacion == '4':
    div, div1 = division(num1, num2)
    print(f"{num1}/{num2} = {div}\n{num2}/{num1} = {div1}")

else:
    print("Seleccione una operación valida")