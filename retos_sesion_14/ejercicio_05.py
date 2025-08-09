def contar_vocales(cadena):
    contador = 0
    cadena = cadena.lower()
    for letra in cadena:
        if letra in "aeiouáéíóú":
            contador += 1
    return contador

print("Cantidad de vocales en 'Hola Mundo':", contar_vocales("Hola Mundo"))


