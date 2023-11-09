while True:
    try:
        nota = float(input("Ingrese una nota entre 0 y 10: "))
        if 0 <= nota <= 10:
            print("La nota es válida.")
            break  # Sale del bucle si la nota es válida
        else:
            print("La nota debe estar entre 0 y 10. Inténtelo nuevamente.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
