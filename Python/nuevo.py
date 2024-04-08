
palabra = input("Ingrese una palabra: ")

palabra = palabra.lower()

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palabra:

    if letra in vocales:
        vocales[letra] += 1

for vocal, conteo in vocales.items():
    print(f"La vocal {vocal} aparece {conteo} veces en la palabra.")
