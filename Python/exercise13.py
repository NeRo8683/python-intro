# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una 
# lista y muestre por pantalla su media y desviación típica.
import math
vecMuestras = []
total = 0
muestras = int(input("Cuantas numeros vas a introducir\n"))
varianza = 0
x = 0
for i in range(muestras):
    muestra = float(input("numero: "+ str(i+1) +"?\n"))
    vecMuestras.append(muestra)

for j in vecMuestras:
    total += j 

media = total/len(vecMuestras)

for k in vecMuestras:
    x+= (k-media)**2

varianza = x/(len(vecMuestras))
desviacion = round(math.sqrt(varianza),2)

print("La media es: "+str(media))
print("La desviacion es: "+str(desviacion))

#print(vecMuestras)

