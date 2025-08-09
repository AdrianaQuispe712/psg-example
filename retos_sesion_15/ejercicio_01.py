while True:
    try:
        num1 = input("Ingrese el primer numero (o 'salir' para terminar): ")
        if num1.lower() == "salir":
            break
        num2 = input("Ingrese el segundo numero (o 'salir' para terminar): ")
        if num2.lower() == "salir":
            break

        num1 = float(num1)
        num2 = float(num2)

        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicacion: {num1 * num2}")
        try:
            print(f"Division: {num1 / num2}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

    except ValueError:
        print("Error: Debe ingresar un valor numerico.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
