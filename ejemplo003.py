"""
Realiza un programa que permita ingresar ingresar valores del mismo tipo para las variables nunUno y
numDos. Una vez cargadas, mostrar ambas variables por pantalla, intercambia sus valores (que lo 
cargado en numUno quede en numDos, y viceversa) y volve a mostrarla actualizadas 
"""

numUno = int(input("Nota 1: "))
numDos = int(input("Nota 2: " ))

print(f"{numUno:3} <---------> {numDos:3}")
auxiliar  = numUno
numUno = numDos
numDos = auxiliar
print(f"{numUno:3} <---------> {numDos:3}")

numUno, numDos = numDos, numUno #solo python
print(f"{numUno:3} <---------> {numDos:3}")