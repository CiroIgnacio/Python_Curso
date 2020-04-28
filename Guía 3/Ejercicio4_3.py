#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:42:45 2020

@author: ciro
"""
#%%
"""Ejercicio 4: Crear una función que, a partir de 4 números, devuelva el mayor producto de dos de ellos. 
Imprimir resultado por pantalla.
"""
def biggestProd(*args):
    args = list(args)
    biggest = max(args)
    args.remove(biggest)
    secondBiggest = max(args)
    return biggest * secondBiggest

print(biggestProd(2,3,4,5,6,7,8,10,11,12,20))
        
    