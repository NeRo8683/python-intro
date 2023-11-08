"""
2.Realize un programa que permita ingresar 3 notas pertenecientes a 3 trimestres distintos
para cierto alumno de nivel secundario. Debe calcularse y mostrarse la nota promedio
"""

numUno = int(input("nota 1: ")) 
numDos = int(input("nota 2: ")) 
numTres = int(input("nota 3: ")) 

prom = numUno + numDos + numTres / 3

print("Notas: ",numUno, numDos, numTres, "Promedio: ",prom)

cadena_formato = f"Notas:{numUno:03}{numDos:03}{numTres:03} ==> Promedio:{prom:8.02}"
print (cadena_formato)