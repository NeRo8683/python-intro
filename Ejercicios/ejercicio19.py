# Dibujar un cuadrado de N elementos por lado utilizando el carácter “*”. Por ejemplo,
# si el cuadrado tiene 4 elementos por lado se deberá dibujar lo siguiente:
# * * * *
# *     *
# *     *
# * * * *


# Solicitar al usuario que ingrese un número entero
num = int(input("Ingrese un número entero para el tamaño del cuadrado: "))

# Dibujar el cuadrado
for i in range(num):
    if i == 0 or i == num - 1:
        print("* " * num)
    else:
        print("* " + "  " * (num - 2) + "*")

