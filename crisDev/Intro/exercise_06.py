# Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso
# actual. Diseñar un algoritmo para este propósito. Recuerda que para calcular el porcentaje
# puedes hacer una regla de 3 simple. El programa debe solicitar al usuario que ingrese la
# cantidad total de niños, y la cantidad total de niñas que hay en el curso

cantidad_ninos = int(input("Ingrese la cantidad total de niños en el curso: "))
cantidad_ninas = int(input("Ingrese la cantidad total de niñas en el curso: "))

# Calcular el porcentaje de niños y niñas
total_alumnos = cantidad_ninos + cantidad_ninas
porcentaje_ninos = (cantidad_ninos / total_alumnos) * 100
porcentaje_ninas = (cantidad_ninas / total_alumnos) * 100

# Mostrar los resultados
print(f"Porcentaje de niños en el curso: {porcentaje_ninos}%")
