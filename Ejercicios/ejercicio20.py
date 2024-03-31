#  Realizar un programa que lea 4 números (comprendidos entre 1 y 20) e imprima el
#  número ingresado seguido de tantos asteriscos como indique su valor. 
#  y luego vuelva a solicitar otro numero hasta q ingrese el numero 0.
#  Por ejemplo:
#  5 *****
#  3 ***
#  11 ***********
#  2 **
#

while True:
    num = int(input("Ingrese un número entero (0 para salir): "))
    
    if num == 0:
        print("Fin del programa.")
        break
    
    print(f"{num} {'*' * num}")
