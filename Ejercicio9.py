#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:42:01 2020

@author: ciro
"""
print("Ingrese 5 números enteros")

numeros = '0123456789-'

lista = []

for i in range(1, 6):
    num = input(f"Número {i}: ")
    lista.append(num)
    
count = 0

for item in lista:
    for j in item:
        if j not in numeros:
            count += 1
if count == 0:
    print(lista)
else:
    print("Usted ha ingresado algún caracter que no pertenece al conjunto de los números enteros. No haga trampa!")