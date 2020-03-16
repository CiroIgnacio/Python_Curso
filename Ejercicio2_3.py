#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:10:34 2020

@author: ciro
"""
#%%
"""
Ejercicio 2: Crear una función que devuelva una lista con todos
los números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.
"""
def evenNums():
    listEven = []
    for i in range(0, 101):
        if i % 2 == 0:
            listEven.append(i)
    for i in listEven:
        print(i, end = " ")

evenNums()
            
