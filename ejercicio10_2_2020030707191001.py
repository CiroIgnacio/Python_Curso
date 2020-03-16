"""Ejercicio 10: Utilizar el método range() para recorrer el iterable e
imprimir solo los números impartes entre 1 y 40 inclusive."""

for i in range(1, 41):
    if not i % 2 == 0:
        print(i, end=" ")