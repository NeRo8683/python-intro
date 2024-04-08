# Escribir un programa que pida al usuario una palabra lo almacene en una lista y muestre por pantalla el 
# número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra:\n") 

vocales = ["a", "e", "i", "o", "u"]

cont = 0
for vocal in vocales:
    cont = 0 
    for letra in palabra:
        if vocal == letra:
            cont += 1

print("La palabra ingresada "+palabra+" tiene: "+str(cont) + vocal)


