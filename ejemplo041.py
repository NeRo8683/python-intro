"""
Ejercicio 41
Escribir un programa que lea numeros enteros hasta que se ingrese un 0 
y muestre el maximo
"""
maximo = float('-inf')
minimo = float('inf')
numero = int(input("numero: "))
hay_datos = False
while numero != 0:
    hay_datos = True
    if numero > maximo:
        maximo = numero
    
    if numero > minimo:
        minimo = numero
    
numero = int(input("numero: "))
#

print(f"maximo: {maximo}")
print(f"minimo: {minimo}")

