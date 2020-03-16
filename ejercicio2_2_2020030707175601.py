"""
Ejercicio 2: Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor.
 Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de la lista.
"""
i = 0
nums = []

while i < 10:
    num = int(input("Introduzca un número: "))
    nums.append(num)
    i += 1

i = 0
bigger = []

for num in nums:
    if num > 100:
        bigger.append(num)
        i += 1

if i >= 3:
    for num in bigger:
        print(num, end = " ")
else:
    for num in nums:
        if num < 50:
            print(num, end = " ")
lower = min(nums)
biggest = max(nums)
print(f"\nEl número mayor es: {biggest}\nEl número menor es: {lower}")
