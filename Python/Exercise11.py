# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla 
# su producto escalar.

vecA = [1, 2, 3]
vecB = [-1, 0, 2]

resultado = 0

for i in range(len(vecA)):
    resultado += vecA[i] * vecB[i]

print("el producto escalar es: "+str(resultado))

numUno = vecA[0] * vecB[0]
numDos = vecA[1] * vecB[1]
numTres = vecA[2] * vecB[2]

resultado2 = numUno+numDos+numTres

print("comprobacion: "+str(resultado2))
