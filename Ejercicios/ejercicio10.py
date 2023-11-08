# Escriba un programa que pida una  palabra que valide si su primera letra es una ‘A’# 

palabra = input("Ingresa una palabra: ")
    
if palabra[0].lower() == 'a':
    print("La primera letra es una 'A'")
else:
    print("La primera letra no es una 'A'")