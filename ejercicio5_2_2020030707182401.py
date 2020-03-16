"""
Ejercicio 5: Crear un diccionario con los meses del año de la forma { 1: "enero"}. Desafío: lograr cambiar las claves. Pista: si imprimen
ítems del diccionario les crea una lista. Una vez que lo logren, imprimir el diccionario modificado.
"""

meses = {1: "enero",
         2: "febrero",
         3: "marzo",
         4: "abril",
         5: "mayo",
         6: "junio",
         7: "julio",
         8: "agosto",
         9: "septiembre",
         10: "octubre",
         11: "noviembre",
         12: "diciembre"}

# Lo que había que hacer
meses_invertido = {}
for keys, values in meses.items():
    meses_invertido[values] = keys
print(meses_invertido)

# Lo que entendí que había que hacer

i = 1

for keys in meses:
    meses[f"Mes {i}"] = meses.pop(i)
    i += 1
    if i == 13:
        break
print(meses)

