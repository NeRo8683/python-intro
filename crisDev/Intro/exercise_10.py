# Crear un programa que solicite al usuario que ingrese el precio de un producto al inicio del
# año, y el precio del mismo producto al finalizar el año. El programa debe calcular cuál fue el
# porcentaje de aumento que tuvo ese producto en el año y mostrarlo por pantalla. 

# Solicitar al usuario que ingrese el precio inicial y final del producto
precio_inicial = float(input("Ingrese el precio del producto al inicio del año: "))
precio_final = float(input("Ingrese el precio del producto al finalizar el año: "))

# Calcular el porcentaje de aumento
aumento = ((precio_final - precio_inicial) / precio_inicial) * 100

# Mostrar el porcentaje de aumento por pantalla
print(f"El porcentaje de aumento del producto en el año fue del {aumento:.2f}%")
