
def encriptar(texto):

    textoFinal = ''
    for i in texto:
        textoFinal += i + "x"
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

    archivo = open(f"{rutaFile}", "r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open("texto.txt", "w")
    archivo.write(textoEncriptado)
    archivo.close()
    print(f"El Archivo {rutaFile} Fue Encriptado Exitosamente! ")


def desencriptarArchivo(rutaFile):

    archivo = open(f"{rutaFile}", "r")
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open("texto.txt", "w")
    archivo.write(textoDesencriptado)
    archivo.close()
    print(f"El Archivo {rutaFile} Fue Desencriptado Exitosamente! ")


elegir = input("Presione la letra 'E' para Encriptar / 'D' para Desencriptar: ").upper()

rutaFile = input('Ingrese la ruta del Archivo: ')

if elegir == 'E':
    encriptarArchivo(rutaFile)
else:
    desencriptarArchivo(rutaFile)
