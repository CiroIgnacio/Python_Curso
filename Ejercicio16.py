#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:16:33 2020

@author: ciro
"""

datos = {}
nombre = input("Introduzca su nombre: ")
datos.update({"Nombre": nombre})
for (keys, values) in datos.items():
    print(f"{keys}: {values}")
    
edad = input("Introduzca su edad: ")
datos.update({"Edad" : edad})
for (keys, values) in datos.items():
    print(f"{keys}: {values}")
    
sexo = input("Introduzca su sexo: ")
datos.update({"Sexo" : sexo})
for (keys, values) in datos.items():
    print(f"{keys}: {values}")

telefono = input("Introduzca su teléfono: ")
datos.update({"Teléfono" : telefono})
for (keys, values) in datos.items():
    print(f"{keys}: {values}")
    
correo = input("Introduzca su correo: ")    
datos.update({"Correo" : correo})
for (keys, values) in datos.items():
    print(f"{keys}: {values}")
