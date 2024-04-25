# A partir de una conocida cantidad de metros que el usuario ingresa a través del teclado se
# debe obtener su equivalente en centímetros, en milímetros y en pulgadas.

# Pedir al usuario que ingrese la cantidad de metros
metros = float(input("Ingrese la cantidad de metros: "))

# Calcular las conversiones
centimetros = metros * 100
milimetros = metros * 1000
pulgadas = metros * 39.3701  # Una pulgada equivale a 0.0254 metros

# Mostrar los resultados
print(f"{metros} metros equivalen a:")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")
print(f"{pulgadas} pulgadas")
