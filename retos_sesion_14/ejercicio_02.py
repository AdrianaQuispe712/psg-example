# 1️⃣ Función para realizar operaciones básicas
def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

print("Suma:", calcular(10, 5, "+"))
print("Resta:", calcular(10, 5, "-"))
print("Multiplicación:", calcular(10, 5, "*"))
print("División:", calcular(10, 5, "/"))


