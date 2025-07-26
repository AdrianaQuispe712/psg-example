print("\nEjercicio 5 Tablero de ajedrez 8x8")
for fila in range(8):
    linea = ""
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            linea += "#"
        else:
            linea += "*"
    print(linea)
