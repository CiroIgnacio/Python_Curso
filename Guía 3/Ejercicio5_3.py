#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:54:19 2020

@author: ciro
"""
#%%
"""
Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números, 
False si hay al menos uno de los parámetros ingresados que no es un número,
y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.
"""
def allNumbers(*args):
    count = 0
    for i in args:
        i = str(i)
        if i.isdigit():
            count += 1
    if count == len(args):
        return True
    elif count == 0:
        return None
    else:
        return False

print(allNumbers('a','asaasas'))
print(allNumbers('121212212121', 'asdsa'))
print(allNumbers('0'))