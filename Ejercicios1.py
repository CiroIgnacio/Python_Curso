#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:02:44 2020

@author: ciro
"""
#%%
print("Hola Mundo!")
#%%
saludo = "Hola Mundo!"
print(saludo)
#%%
nombre = input("Ingresá tu nombre: ")
edad = input("Ingresá tu edad: ")
print("Nombre:{0}\nEdad:{1}".format(nombre,edad))
#%%
nombre = input("Ingresá tu nombre: ")
print("¡Hola {}!".format(nombre))
#%%
numero1 = int(input("Ingresa un número: "))
numero2 = int(input ("Ingresa otro número: " ))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1//numero2
print("Suma = {0}\nResta = {1}\nMultiplicación = {2}\nDivisión = {3}".format(suma,resta,multiplicacion,division))
#%%
deposito = 2000 
interes = 2000*0.05
total = deposito + interes
print(total)
#%%
pagoPorHora = 400
horasPorDia = 8
diasSemana = 5
sueldo = 400*8*5*4
print(sueldo)
#%%
materias = ["Historia", "Matemáica", "Lengua", "Geografía"]
print(materias[-1])
#%%
num1 = input("Numero 1: ")
num2 = input("Numero 2: ")
num3 = input("Numero 3: ")
num4 = input("Numero 4: ")
num5 = input("Numero 5: ")

lista = [num1,num2,num3,num4,num5]
print(lista)
#%%
lista = []
for i in range(5):
    num = input("Número: ")
    lista.append(num)
    
print(lista)
#%%
abc = "abcdefghijklmnñopqrstuvwxyz"
abc_lista = list(abc)
vocales = "aeiou"
vocales_lista = list(vocales)
lista_nueva = []

for i in abc_lista:
    if i not in vocales_lista:
        lista_nueva.append(i)

print(lista_nueva)
#%%
numeros = [9, 2, 5, 7, 1]
numeros.sort()
menor = numeros[0]
maximo = numeros[-1]
print(f"Lista: {numeros}\nMenor: {menor}\nMayor:{maximo}")
#%%
v1 = [1, 2, 3]
v2 = [-1, 0, 2]

prodEscalar1 = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
prodEscalar = 0

for i in range(3):
    prod = v1[i]*v2[i]
    prodEscalar += prod

print(prodEscalar)
print(prodEscalar1)
#%%
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduzca una divisa: ")  
divisa = divisa.title()
claves = list(divisas.keys())  


if divisa in claves:
    print(divisas[divisa])
else:
    print("Divisa no encontrada")

    
#%%
nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
direccion = input("Introduzca su dirección: ")
telefono = input("Introduzca su teléfono: ")
datos = {"Nombre" : nombre, "Edad" : edad, "Direccion" : direccion, "Teléfono" : telefono}
print(datos)
#%%
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
for (keys, values) in asignaturas.items():
    print(f"{keys} tiene {values} créditos")
#%%
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




    


