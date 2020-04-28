#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:14:20 2020

@author: ciro
"""
#%%

"""
Ejercicio 10: Crear una función decoradora para una función matemática cualquiera.
"""
from math import sqrt
def decoraRaiz(funcion):
    def funcionInterna(a):
        print("="*12)
        print(f"Ejecutando la {funcion.__name__} cuadrada de {a}")
        print("="*12)
        funcion(a)
        print("="*12)
        print("Ejecución finalizada con éxito :)")
    return funcionInterna

@decoraRaiz
def raiz(a):
    result = round(sqrt(a), 2)
    print(f"El resultado es {result}")

raiz(200)
