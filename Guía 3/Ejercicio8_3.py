#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:21:06 2020

@author: ciro
"""
#%%
"""
Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta 
un auto que consume 2 litros x 100km, en un viaje ida y vuelta MdP-Bue si 
la distancia es de 400km. Luego crear una función que, a partir de esos datos, 
devuelva cuánto significa eso en pesos si el litro de nafta está 60$.
"""
def consumoNafta(kms):
    return 0.02 * kms

def costoNafta(precioLitro, kms):
    return precioLitro * consumoNafta(kms)

print(costoNafta(60, 400))
