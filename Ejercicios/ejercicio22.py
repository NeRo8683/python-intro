# Realizar un algoritmo que rellene una tupla con los 100 primeros números enteros y
# los muestre por pantalla en orden descendente

# Crear una tupla con los 100 primeros números enteros
tupla_numeros = tuple(range(1, 101))
# Convertir la tupla en una lista para ordenarla en orden descendente
lista_numeros_descendente = sorted(tupla_numeros, reverse=True)
# Mostrar los números en orden descendente
print(lista_numeros_descendente)
print("------------")
# Realizar un algoritmo que rellene un vector con los 100 primeros números enteros y
# los muestre por pantalla en orden descendente

# Crear un vector con los 100 primeros números enteros
vector = list(range(1, 101))
# Mostrar el vector en orden descendente
vector.reverse()
print(vector)
