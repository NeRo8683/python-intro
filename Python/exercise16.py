# Inicializar una variable para contar los números leídos
contador = 0
suma_numeros = 0
# Bucle while para leer 8 números
while contador < 8:
    # Pedir al usuario que ingrese un número
    numero = int(input("Ingrese un número: "))    
    
    # Verificar si el número es cero
    if numero == 0:
        print("Se capturó el número cero.")
        break  # Salir del bucle si se captura el número cero
    
    # Incrementar el contador de números leídos
    contador += 1
    # Sumar el número si es positivo
    if numero > 0:
        suma_numeros += numero

# Mostrar la suma de los números positivos
print(f"La suma de los números positivos es: {suma_numeros}")


# Mensaje de fin del programa
print("Fin del programa.")