class FrutaInvalidaError(Exception):
    pass

frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
canasta = []

while True:
    try:
        fruta = input("Ingrese una fruta (o 'salir' para terminar): ")
        if fruta.lower() == "salir":
            break
        if fruta not in frutas_permitidas:
            raise FrutaInvalidaError("Fruta no permitida.")
        canasta.append(fruta)
    except FrutaInvalidaError as e:
        print(f"Error: {e}")

print("Canasta final:", canasta)
