#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:16:05 2020

@author: ciro
"""

"""
Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no. 
En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", 
en caso contrario, devolver "La palabra no es un palíndromo".
"""

#%%
def isPalindrome(word):
    if word  == word[::-1]:
        return f"La palabra {word} es un palíndromo"
    else:
        return f"La palabra {word} no es un palíndromo"
    
print(isPalindrome("neuquen"))
print(isPalindrome("casa"))