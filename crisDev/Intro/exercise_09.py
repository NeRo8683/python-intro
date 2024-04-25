# A partir de una conocida cantidad de días que el usuario ingresa a través del teclado, escriba
# un programa para convertir los días en horas, en minutos y en segundos. Por ejemplo
# 1 día = 24 horas = 1440 minutos = 86400 segundos

# Solicitar al usuario que ingrese la cantidad de días
dias = int(input("Ingrese la cantidad de días: "))

# Calcular las conversiones
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

# Mostrar los resultados
print(f"{dias} días equivalen a:")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")
