# Teniendo en cuenta el numero pi pedir al usuario que ingrese el valor del radio de una 
# circunferencia y calcular y mostrar por pantalla el área y perímetro.

import math

radio = float(input("Ingrese el valor del radio de la circunferencia: "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área de la circunferencia es: {area}")
print(f"El perímetro de la circunferencia es: {perimetro}")
