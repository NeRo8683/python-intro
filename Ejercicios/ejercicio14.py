# Escriba un programa en el cual se ingrese un valor límite positivo, y a continuación
# solicite números al usuario hasta que la suma de los números introducidos supere
# el límite inicial.


limite = int(input("Ingrese un valor límite positivo: "))

while limite <= 0:
    print("El valor límite debe ser positivo.")
    limite = int(input("Ingrese un valor límite positivo: "))

suma_numeros = 0
contador = 0

while suma_numeros <= limite:
    numero = int(input("Ingrese un número: "))
    suma_numeros += numero
    contador += 1

print(f"La suma total de los números ingresados es: {suma_numeros}")
print(f"Se ingresaron {contador} números para superar el límite.")