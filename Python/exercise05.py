# Escribir un programa que pida al usuario al usuario una cantidad de dinero a invertir, la tasa de interés 
# anual y el número de años, y muestre por pantalla el capital obtenido en la inversión durante cada año

cant=float(input("cantidad a invertir: "))
interes=float(input("porcentaje de interes: "))
año=int(input("Años: "))

for i in range(año):
  cant *=1+ interes/100

print("capital obtenido tras " + str(i+1) + " años: " + str(round(cant ,2)) )





