def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    return texto == texto[::-1]

frase = input("Ingrese una frase : ")
print("Es palindromo?", es_palindromo(frase))
