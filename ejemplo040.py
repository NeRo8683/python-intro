"""
Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b.
El programa debe mostrar: la suma de os numeros pares entre a y b, y
el producto de los numeros impares entre a y b. 
"""

a = int(input('Ingrese un numero: '))
b = int(input('Ingrese un numero: '))
numeroSumados = ''
numerosMultiplicados = ''
suma = 0
producto = 1
for i in range(a, b+1):
    if i%2 == 0:
        suma += i
        numeroSumados += f"{i} "
    else:
        numeroSumados += f"{i} "
        producto *=i
print(f'Suma ==> {suma} [{numeroSumados}]')
print(f'Producto ==> {producto} [{numerosMultiplicados}]')















