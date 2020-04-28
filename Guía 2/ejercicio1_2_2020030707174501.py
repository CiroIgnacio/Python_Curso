"""Pedir al usuario que ingrese un mensaje cualquiera, si el mensaje tiene más de 100 caracteres imprimirlo por teclado,
si tiene hasta 50 caracteres imprimirlo al revés, si no se cumple ninguna de las opciones anteriores, por pantalla devolver
un mensaje que diga "su mensaje es demasiado corto"""

msg = input("Introduzca un mensaje: ")
msgLenght = len(msg)


if msgLenght > 100:
    print(msg)

elif msgLenght >= 50:
    msg = list(msg)
    print(msg)
    msg.reverse()
    msg = "".join(msg)
    print(msg)


else:
    print("Su mensaje es demasiado corto")