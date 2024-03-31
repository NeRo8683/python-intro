# Realizar un algoritmo que rellene un vector de tamaño N con valores aleatorios y le pida al usuario un 
# numero a buscar en el vector. El programa mostrará donde se encuentra el numero y si se encuentra repetido
#
#

import random

# Función para generar un vector de tamaño N con valores aleatorios
def generar_vector(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

# Función para buscar un número en el vector y verificar si está repetido
def buscar_numero(vector, numero):
    posiciones = []
    repetido = False
    
    for i, num in enumerate(vector):
        if num == numero:
            posiciones.append(i)
            repetido = True if posiciones.count(i) > 1 else False
    
    return posiciones, repetido

# Pedir al usuario el tamaño del vector
N = int(input("Ingrese el tamaño del vector: "))

# Generar el vector con valores aleatorios
vector = generar_vector(N)

# Mostrar el vector generado
print("Vector generado:", vector)

# Bucle para buscar el número en el vector
while True:
    # Pedir al usuario el número a buscar
    numero_buscar = int(input("Ingrese el número a buscar en el vector: "))

    # Salir del bucle si se ingresa el número 0
    if numero_buscar == 0:
        print("0 capturado")
        print("Fin del programa.")
        break
    
    # Buscar el número en el vector y verificar si está repetido
    posiciones_numero, es_repetido = buscar_numero(vector, numero_buscar)
    
    # Mostrar los resultados
    if posiciones_numero:
        print(f"El número {numero_buscar} se encuentra en las posiciones:", posiciones_numero)
        
        if es_repetido:
            print(f"El número {numero_buscar} está repetido en el vector.")
        else:
            print(f"El número {numero_buscar} no está repetido en el vector.")
        
        # Salir del bucle y del programa
        print("Fin del programa.")
        break
    else:
        print(f"El número {numero_buscar} no se encuentra en el vector.")
