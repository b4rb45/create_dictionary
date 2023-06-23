import string
import random


def generar_diccionario(cantidad_palabras, largo_palabra, incluir_letras, incluir_numeros, incluir_caracteres_especiales):
    caracteres = ""
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    diccionario = []
    while len(diccionario) < cantidad_palabras:
        palabra = ''.join(random.choice(caracteres) for _ in range(largo_palabra))
        diccionario.append(palabra)

    return diccionario


def guardar_diccionario(diccionario, archivo):
    with open(archivo, 'w') as file:
        for palabra in diccionario:
            file.write(palabra + '\n')


def main():
    cantidad_palabras = int(input("Ingrese la cantidad de palabras para el diccionario: "))
    largo_palabra = int(input("Ingrese el largo de cada palabra: "))
    incluir_letras = input("Incluir letras en las palabras (S/N): ").lower() == 's'
    incluir_numeros = input("Incluir nÃºmeros en las palabras (S/N): ").lower() == 's'
    incluir_caracteres_especiales = input("Incluir caracteres especiales en las palabras (S/N): ").lower() == 's'
    archivo = input("Ingrese el nombre del archivo para guardar el diccionario: ")

    diccionario = generar_diccionario(
        cantidad_palabras, largo_palabra, incluir_letras, incluir_numeros, incluir_caracteres_especiales
    )
    guardar_diccionario(diccionario, archivo)

    print("Diccionario generado y guardado exitosamente.")


if __name__ == '__main__':
    main()
