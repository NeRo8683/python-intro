# Realiza un programa que sólo permita introducir los caracteres ‘S’ y ‘N’. Si el usuario ingresa 
# alguno de esos dos caracteres se deberá de imprimir un mensaje por pantalla que diga “CORRECTO”, 
# en caso contrario, se deberá imprimir “INCORRECTO”.#

# Solicitar al usuario que ingrese un carácter
caracter = input("Ingrese un carácter ('S' o 'N'): ")

# Verificar si el carácter es 'S' o 'N' y mostrar un mensaje
if caracter == 'S' or caracter == 'N':
    print("CORRECTO")
else:
    print("INCORRECTO")


