import string
import random

CHARACTERS = string.ascii_letters + string.digits + string.punctuation


def encriptar(texto):

    textoFinal = ''
    for i in texto:

        textoFinal += i + random.choice(CHARACTERS)

    return textoFinal


def desencriptar(texto):

    textoFinal = ''
    contador = 0
    for i in texto:
        if contador % 2 == 0:
            textoFinal += i
        contador += 1
    return textoFinal


def encriptarArchivo(rutaFile):

    with open(rutaFile, "r") as archivo:
        texto = archivo.read()
        textoEncriptado = encriptar(texto)

    with open(rutaFile, "w") as archivo:
        archivo.write(textoEncriptado)

    print(f"El Archivo {rutaFile} Fue Encriptado Exitosamente! ")


def desencriptarArchivo(rutaFile):

    with open(rutaFile, "r") as archivo:
        texto = archivo.read()
        textoDesencriptado = desencriptar(texto)

    with open(rutaFile, "w") as archivo:
        archivo.write(textoDesencriptado)

    print(f"El Archivo {rutaFile} Fue Desencriptado Exitosamente! ")


elegir = input(
    "Presione la letra 'E' para Encriptar / 'D' para Desencriptar: ").upper()

rutaFile = input('Ingrese la ruta del Archivo: ')

if elegir == 'E':
    encriptarArchivo(rutaFile)
else:
    desencriptarArchivo(rutaFile)
