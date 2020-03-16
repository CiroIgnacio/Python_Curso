#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:30:46 2020

@author: ciro
"""
#%%
"""
Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas.
Luego crear una función que nos informe los estudiantes aprobados (nota >= 7), 
los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).
"""
def evalua(dic):
    aprobados = []
    desaprobados = []
    aplazados = []
    for keys, values in dic.items():
         if values["Nota"] >= 7:
            aprobados.append(values["Nombre"])
         elif 4 <= values["Nota"] < 7:
             desaprobados.append(values["Nombre"])
         else:
             aplazados.append(values["Nombre"])
    return aprobados, desaprobados, aplazados
ID = 0
estudiantes = {}
while ID < 10:
    print(f"Alumno {ID}", end ="")
    nombre = input("Nombre: ")
    try:
        nota = int(input("Nota: "))
        estudiantes[ID] = {"Nombre": nombre, "Nota": nota}
        ID += 1
    except ValueError:
        print("La nota debe ser un valor numérico")
    
aprobados, desaprobados, aplazados = evalua(estudiantes)

if aprobados: 
    print("Alumnos aprobados:")
    for i in aprobados:
        print(i)
else:
    print("No hay alumnos aprobados")
if desaprobados:
    print("Alumnos desaprobados:")
    for i in desaprobados:
        print(i)
else:
    print("No hay alumnos desaprobados")
if aplazados:
    print("Alumnos aplazados:")
    for i in aplazados:
        print(i)
else:
    print("No hay alumnos aplazados")


