# Escribir un programa que almacene en una lista los siguientes numeros  50, 75, 46, 22, 80, 65, 8, y 
# muestre por pantalla el menor y el mayor.
# 

num = [50, 75, 46, 22, 80, 65, 8] 
#min = max = num[0]
min =  num[0]
max =  num[0]

for numero in num:
    if numero < min:
        min = numero
    elif numero > max:
        max = numero

print("El maximo es "+str(max))
print("El minimo es "+str(min))





