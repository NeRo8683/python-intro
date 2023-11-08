# Escribir un programa que lea un número entero y muestre por pantallael doble, el triple y la raíz cuadrada
# de ese número

import math
print("Ingrese un numero")
numUno = int(input())

mitad = numUno / 2
doble = numUno*2
cuadrado = numUno**2
triple = numUno*3
raiz = math.sqrt(numUno)

print("mitad:",mitad)
print("doble:",doble)
print("cuadrado:",cuadrado)
print("triple:",triple)
print("raiz:",raiz)
