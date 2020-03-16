#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:04:23 2020

@author: ciro
"""
#%%
"""Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea en horas, 
nos informe cuántos minutos y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.
"""

def hoursToMin(hours):
    return hours * 60

def hoursToSec(hours):
    return hoursToMin(hours) * 60

def converter(hours):
    conv = f"Hours = {hours}\nMinutes = {hoursToMin(hours)}\nSeconds = {hoursToSec(hours)}"
    return conv
    
print(converter(6))
