#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:10:46 2020

@author: ciro
"""
print("Este programa realizará las 4 operaciones matemáticas básicas entre dos números elegidos")
try:
    numero1 = float(input("Ingresa un número: "))
    numero2 = float(input ("Ingresa otro número: " ))
    suma = numero1 + numero2
    resta = numero1 - numero2
    resta1 = numero2 - numero1
    multiplicacion = numero1 * numero2
    
    try:
        division = numero1/numero2
        division1 = numero2/numero1
    except ZeroDivisionError:
        division = None;
        print("\nDividir por cero no es una operación válida\n")
    try:
        division1 = numero2/numero1
    except ZeroDivisionError:
        division1 = None;
        print("Dividir por cero no es una operación válida\n")
    
        
    print("{4} - {5} = {0}\n{5} - {4} = {1}\n{4} + {5} = {2}\n{4} * {5} = {3}\n{4}/{5} = {6}\n{5}/{4} = {7} ".format(resta, resta1, suma, multiplicacion, numero1, numero2, division, division1))
    
except ValueError:
    print("Por favor ingrese un número")
