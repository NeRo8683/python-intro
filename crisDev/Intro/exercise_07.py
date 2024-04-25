# Solicitar al usuario que ingrese la base y altura de un rectángulo, y calcular y mostrar por
# pantalla el área y perímetro del mismo

# Solicitar al usuario que ingrese la base y altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el área y el perímetro del rectángulo
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar los resultados por pantalla
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")
