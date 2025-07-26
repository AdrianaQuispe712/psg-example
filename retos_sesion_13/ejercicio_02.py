print("\nEjercicio 2 Múltiplos de 2 y 5")
contador = 0
numero = 1
while contador < 20:
    if numero % 2 == 0 and numero % 5 == 0:
        print(numero, end=" ")
        contador += 1
    numero += 1
