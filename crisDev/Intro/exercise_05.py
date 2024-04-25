# Escriba un programa que permita al usuario ingresar el valor de dos variables numéricas de
# tipo entero. Posteriormente, el programa debe intercambiar los valores de ambas variables y
# mostrar el resultado final por pantalla. 

# Pedir al usuario que ingrese el valor de las dos variables
valor_1 = int(input("Ingrese el valor de la primera variable entera: "))
valor_2 = int(input("Ingrese el valor de la segunda variable entera: "))

# Intercambiar los valores de las variables
temporal = valor_1
valor_1 = valor_2
valor_2 = temporal

# Mostrar el resultado final
print("Después de intercambiar los valores:")
print(f"Valor de la primera variable: {valor_1}")
print(f"Valor de la segunda variable: {valor_2}")
