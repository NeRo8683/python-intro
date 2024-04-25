# Escribir un programa que calcule el precio promedio de un producto. El precio promedio se
# debe calcular a partir del precio del mismo producto en tres establecimientos distintos

precio_establecimiento_1 = float(input("Ingrese el precio del producto en el establecimiento 1: "))
precio_establecimiento_2 = float(input("Ingrese el precio del producto en el establecimiento 2: "))
precio_establecimiento_3 = float(input("Ingrese el precio del producto en el establecimiento 3: "))

precio_promedio = (precio_establecimiento_1 + precio_establecimiento_2 + precio_establecimiento_3) / 3

print(f"El precio promedio del producto es: {precio_promedio}")
