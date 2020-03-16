#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:26:20 2020

@author: ciro
"""

nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
direccion = input("Introduzca su dirección: ")
telefono = input("Introduzca su teléfono: ")
datos = {"Nombre" : nombre, "Edad" : edad, "Direccion" : direccion, "Teléfono" : telefono}

for keys, values in datos.items():
    print(f"{keys}: {values}")