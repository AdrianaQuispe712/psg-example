tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

turno = "X"

def mostrar_tablero():
    for fila in tablero:
        print(fila)

def verificar_ganador():
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != " ":
            return True
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False

def tablero_lleno():
    for fila in tablero:
        for celda in fila:
            if celda == " ":
                return False
    return True

def tres_en_raya(jugador, fila, columna):
    global turno

    if tablero[fila][columna] != " ":
        print("Casilla ocupada, elige otra.")
        return

    if jugador != turno:
        print("No es tu turno.")
        return

    tablero[fila][columna] = jugador
    mostrar_tablero()

    if verificar_ganador():
        print(f"¡Jugador {jugador} gana!")
        return

    if tablero_lleno():
        print("¡Empate!")
        return

    turno = "O" if turno == "X" else "X"
    print(f"Juega '{turno}'")

tres_en_raya("X", 0, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 0, 1)
tres_en_raya("O", 2, 2)
tres_en_raya("X", 0, 2)  
