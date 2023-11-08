# Ingrese una palabra que si tiene 8 caracteres de largo  imprima un mensaje por pantalla que diga CORRECTO 
# sino que diga INCORRECTO

palabra = input("Ingresa una palabra: ")
    
if len(palabra) == 8:
    print("CORRECTO")
else:
    print("INCORRECTO")
