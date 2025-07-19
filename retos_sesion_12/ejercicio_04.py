edad = int(input("Ingrese su edad: "))
compra = float(input("Ingrese el monto de su compra: "))
if edad > 60 and compra > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and compra > 500:
    descuento = 0.10
else:
    descuento = 0.02
monto_final = compra * (1 - descuento)
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Monto a pagar: {monto_final:.2f}")
