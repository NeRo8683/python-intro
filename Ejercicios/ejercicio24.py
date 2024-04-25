# Inicializar contadores para cada categoría de dígitos
contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# Pedir al usuario que ingrese 5 números enteros uno por uno
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    longitud = len(str(numero))
    
    # Incrementar el contador correspondiente
    if longitud <= 5:
        contadores[longitud] += 1

# Mostrar los resultados
for longitud, contador in contadores.items():
    print(f"Cantidad de números de {longitud} dígitos:", contador)
