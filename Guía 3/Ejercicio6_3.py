#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:06:39 2020

@author: ciro
"""

"""
Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title. 
Si el mensaje ya está en modo title,
 que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"
"""
#%%
def modeTitle(msg):
    if msg.istitle():
        return f"El mensaje ya está en modo title: {msg}"
    else:
        return f"El mensaje en modo title es: {msg.title()}"

print(modeTitle('Hola Como Estas'))
print(modeTitle('Hola como estas'))