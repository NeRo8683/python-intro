# Escribir un programa que calcule cuántos litros de combustible consumió un automóvil. El
# usuario ingresará una cantidad de litros de combustible cargados en la estación y una
# cantidad de kilómetros recorridos, después, el programa calculará el consumo (km/lt) y se lo
# mostrará al usuario.

# Pedir al usuario que ingrese la cantidad de litros de combustible y los kilómetros recorridos
litros_combustible = float(input("Ingrese la cantidad de litros de combustible cargados: "))
kilometros_recorridos = float(input("Ingrese la cantidad de kilómetros recorridos: "))

# Calcular el consumo en kilómetros por litro (km/lt)
consumo = kilometros_recorridos / litros_combustible

# Mostrar el consumo al usuario
print(f"El consumo del automóvil es de {consumo} km por litro")
