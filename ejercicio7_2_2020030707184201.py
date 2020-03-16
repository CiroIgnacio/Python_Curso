"""Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir por pantalla los alumnos
que aprobaron y su nota (no en forma de diccionario, si no con nombre : nota). Tener en cuenta que para aprobar el
alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10."""

i = 1
alumnos = [f"Alumno {i}" for i in range(1, 6)]
notas = []
while i < 6:
    nota = int(input(f"Alumno {i}: "))
    notas.append(nota)
    i += 1

diccionarioNotas = dict(zip(alumnos, notas))

print("Alumnos que aprobaron:")

aprobados = False

for keys, values in diccionarioNotas.items():
    if 7 <= values <= 10:
        print(f"{keys} con nota = {values}")
        aprobados = True

if not aprobados:
    print("Ninguno :(")