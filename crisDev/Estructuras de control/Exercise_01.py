# Un hombre desea saber si su sueldo es mayor al sueldo mínimo, el algoritmo le pedirá al usuario su 
# sueldo actual y el sueldo mínimo. Si el sueldo es mayor al mínimo se debe mostrar un mensaje por 
# pantalla indicándolo.

# Solicitar al usuario que ingrese su sueldo actual y el sueldo mínimo
sueldo_actual = float(input("Ingrese su sueldo actual: "))
sueldo_minimo = float(input("Ingrese el sueldo mínimo: "))

# Verificar si el sueldo es mayor al mínimo y mostrar un mensaje
if sueldo_actual > sueldo_minimo:
    print("Su sueldo es mayor al sueldo mínimo.")
else:
    print("Su sueldo no es mayor al sueldo mínimo.")
