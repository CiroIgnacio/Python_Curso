#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:11:16 2020

@author: ciro
"""

abc = "abcdefghijklmnñopqrstuvwxyz"
abc_lista = list(abc)
vocales = "aeiou"
vocales_lista = list(vocales)
lista_nueva = []

for i in abc_lista:
    if i not in vocales_lista:
        lista_nueva.append(i)

print(lista_nueva)