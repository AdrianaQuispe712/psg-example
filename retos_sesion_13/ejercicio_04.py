print("\nEjercicio 4 Verificar palindromos")
while True:
    frase = input("Ingresa una frase (o escribe 'salir' para terminar): ")
    if "salir" in frase:
        break
    frase_sin_espacios = frase.replace(" ", "").lower()
    if frase_sin_espacios == frase_sin_espacios[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
