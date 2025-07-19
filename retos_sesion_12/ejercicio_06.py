entrada = input("Operacin: ")  
partes = [p.strip() for p in entrada.split(",")]
if len(partes) != 3:
    print("Entrada invalida. Formato correcto: numero1, numero2, operacion")
else:
    num1_str, num2_str, oper = partes
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Numeros invalidos")
    else:
        if oper not in ['+', '-', '*', '/']:
            print("Operacion invalida")
        else:
            if oper == '+':
                resultado = num1 + num2
            elif oper == '-':
                resultado = num1 - num2
            elif oper == '*':
                resultado = num1 * num2
            else: 
                if num2 == 0:
                    print("Error: Division por cero")
                    resultado = None
                else:
                    resultado = num1 / num2
            if resultado is not None:
                if resultado.is_integer():
                    resultado = int(resultado)
                print(f"Resultado: {resultado}")
