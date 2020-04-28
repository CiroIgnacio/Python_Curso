#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:22:06 2020

@author: ciro
"""

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduzca una divisa: ")  
divisa = divisa.lower().title()

claves = list(divisas.keys())  

if divisa in claves:
    print(divisas[divisa])
else:
    print("Divisa no encontrada")