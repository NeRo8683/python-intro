# suma = 0
# numero = int (input("ingrese un numero"))
# while numero!=0:
#     suma = suma + 1
#     numero = int (input("ingrese un numero"))
# print(f"la suma es: {suma}")

# suma = 0
# cantidad = 10
# for contador in range(cantidad):
#     # DURANTE
#     numero = int(input(f"ingrese el {contador} de {cantidad} Numero:"))
#     suma = suma + numero
# print(f"La suma es: {suma}")

"""
cantidad = 10
for contador in range(1, cantidad+1):
    # DURANTE
    numero = int(input(f"ingrese el {contador} de {cantidad} Numero:"))
    suma = suma + numero

print(f"La suma es: {suma}")


for letra in "lumberjack":
    print (letra)



cantidad_letras = len(letra)
for x in range(cantidad_letras):
    print(letra[x]) 

"""

import whisper
import os
from docx import Document

# Cargar modelo de transcripción
model = whisper.load_model("base")

# Transcribir el archivo de audio
audio_file_path = "/content/drive/MyDrive/Whisper/Abril 4 - Régimen patrimonial. Gestión y pasivo - Nadia Tordi.WAV"
result = model.transcribe(audio_file_path)
text = result["text"]

# Crear y guardar archivo Word con el texto transrito
docx_file_path = os.path.splitext(audio_file_path)[0] + ".docx"
document = Document()
document.add_paragraph(text)
document.save(docx_file_path)

print(f"Archivo Word guardado en {docx_file_path}")