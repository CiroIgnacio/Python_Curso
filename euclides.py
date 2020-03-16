#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:44:40 2019

@author: ciro
"""

#Programa sencillo para detectar el maximo común divisor entre dos núms usando el algoritmo de euclides
x = input("x: ")
y = input("y: ")
if x.isdigit() and y.isdigit():
    x = int(x)
    y = int(y)
    bool = 1
    msg = "El MCD entre " + str(x) + " y "+ str(y) + " es:"

    while bool == 1:
        if x<y:
            y = y-x
        elif y<x:
            x = x-y
        elif x == y:
            print(msg,x)
            bool = 0
else:
    print("\nDebe ingresar números")

#%%
    print("hola")
    
#%%
    