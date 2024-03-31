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
