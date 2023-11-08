"""
Ejercicio 049
Escribir un programa que permita valida una opcion ingresada. Se le preguntara al 
usuario si desea continuar con alguna operacion de la forma "¿Desea continuar?[S/N].
Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minusculas). La opcion
debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las 
posibilidades esperadas.
"""

opcion = input("Continua? [S/N]:").upper()
while opcion is not ('S', 'N'):
    print(f"{opcion} No es valida")
    opcion = input("Continua [S/N] :").upper
print(opcion)