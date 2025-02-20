# Encriptador y Desencriptador de Archivos

Este es un script en Python que permite encriptar y desencriptar archivos de texto agregando caracteres aleatorios a cada letra del texto original.

## Requisitos

Este script utiliza únicamente librerías estándar de Python, por lo que no es necesario instalar dependencias adicionales.

## Uso

1. Ejecuta el script en la terminal o en un entorno de Python.
2. Selecciona una opción:
   - Presiona `E` para encriptar un archivo.
   - Presiona `D` para desencriptar un archivo.
3. Ingresa la ruta del archivo que deseas procesar.
4. El archivo se encriptará o desencriptará y se sobrescribirá con el nuevo contenido.

## Funcionamiento

- **Encriptación:**
  - La función `encriptar(texto)` toma un texto y añade un carácter aleatorio después de cada letra.
  - La función `encriptarArchivo(rutaFile)` abre el archivo, encripta su contenido y lo sobrescribe con el nuevo contenido encriptado.

- **Desencriptación:**
  - La función `desencriptar(texto)` elimina los caracteres adicionales, dejando solo el texto original.
  - La función `desencriptarArchivo(rutaFile)` abre el archivo, desencripta su contenido y lo sobrescribe con el texto original.

## Precauciones

- Asegúrate de realizar una copia de seguridad del archivo antes de encriptarlo.
- Este método de encriptación no es seguro para proteger información sensible, ya que es fácilmente reversible.

