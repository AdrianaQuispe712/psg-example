print("\nEjercicio 6 - Verificar múltiplos de 7")
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    if numero % 7 == 0:
        print("Es múltiplo de 7")
    else:
        print("No es múltiplo de 7")
