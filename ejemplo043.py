"""
Ejercicio 043
Escribir un programa que lea numeros enteros hasta que la suma de los numeros
sea mayor que 100, y muestre la cantidad de numeros ingresados
"""
import random
numero = random.randint(1, 10)
contador = 0
suma = 0
while suma < 100:
    print(f"Numero: {numero} Suma: {suma} Cantidad: {contador}") 
    contador = contador + 1
    suma = suma + numero
    numero = random.randint(1, 10)
print(f"Cantidad de numeros: {contador}")
