"""
Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.
"""
i = 0
nums = []
while i < 6:
    try:
        num = int(input("Ingrese un número: "))
        nums.append(num)
        i += 1
    except ValueError:
        print("Por favor ingrese números enteros!")

nums.sort()

for num in nums:
    print(num, end=" ")
