# Escriba un programa que lea 8 números. Si el número leído es igual a cero se debe
# salir del bucle y mostrar el mensaje "Se capturó el numero cero". El programa
# deberá calcular y mostrar el resultado de la suma de los números leídos, pero si el
# número es negativo no debe sumarse. Nota: recordar el uso de la sentencia break.


# Inicializar la variable para almacenar la suma de números
suma_numeros = 0

# Leer 8 números
for i in range(1, 9):
    numero = int(input(f"Ingrese el número {i}: "))
    
    # Salir del bucle si el número es cero
    if numero == 0:
        print("Se capturó el número cero.")
        break
    
    # Sumar el número si es positivo
    if numero > 0:
        suma_numeros += numero

# Mostrar la suma de los números positivos
print(f"La suma de los números positivos es: {suma_numeros}")
