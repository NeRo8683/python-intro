# Implementar un programa que dado dos números enteros determine cuál es el
# mayor y lo muestre por pantalla

print("Ingrese numero Uno")
numUno = int(input())
print("Ingrese numero Dos")
numDos = int(input())

if numUno == numDos:
    print("son iguales")
else:
    if numUno > numDos:
        print(f"El numero mayor es", numUno)
    else:
        print(f"El numero mayor es", numDos)