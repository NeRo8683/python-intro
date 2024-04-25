# Escribir un programa que calcule el volumen de un cilindro. Para ello se deberá solicitar al
# usuario que ingrese el radio y la altura. Mostrar el resultado por pantalla.

import math

# Solicitar al usuario que ingrese el radio y la altura del cilindro
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular el volumen del cilindro
volumen = math.pi * radio**2 * altura

# Mostrar el resultado por pantalla
print(f"El volumen del cilindro es: {volumen}")

