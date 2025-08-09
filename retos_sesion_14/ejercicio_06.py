def separar_pares_impares(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros = [1, 2, 3, 4, 5, 6]
pares, impares = separar_pares_impares(numeros)
print("Pares:", pares)
print("Impares:", impares)


