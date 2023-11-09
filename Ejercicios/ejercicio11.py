tipoMotor = input("Ingrese un valor entre 1 y 4 para el tipo de motor: ")

if tipoMotor == "1":
    print("La bomba es una bomba de agua")
elif tipoMotor == "2":
    print("La bomba es una bomba de gasolina")
elif tipoMotor == "3":
    print("La bomba es una bomba de hormigón")
elif tipoMotor == "4":
    print("La bomba es una bomba de pasta alimenticia")
else:
    print("No existe un valor válido para tipo de bomba")