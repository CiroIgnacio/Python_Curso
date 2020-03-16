#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:14:18 2020

@author: ciro
"""

"""
Ejercicio 3: Crear una función que, a partir de un mensaje, nos devuelva una lista
con todos los números, si los hay, que aparecen en dicho mensaje.
"""
#%%
def digits(msg):
    digitsList = []
    for char in msg:
        if char.isdigit():
            digitsList.append(char)
    digitsList = list(set(digitsList))
    return digitsList

mensaje = input("Introduzca un mensaje: ")
print("Los números que aparecen en su mensaje son: ")
for i in digits(mensaje):
    print(i, end = " ")