class FondosInsuficientesError(Exception):
    pass

saldo = 500
limite_transaccion = 1000

try:
    monto = float(input("Ingrese el monto a retirar: "))
    if monto > limite_transaccion:
        raise Exception("Monto excede el límite permitido por transacción.")
    if monto > saldo:
        raise FondosInsuficientesError("Fondos insuficientes.")
    saldo -= monto
    print(f"Retiro exitoso. Saldo restante: {saldo}")
except FondosInsuficientesError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Debe ingresar un valor numérico.")
except Exception as e:
    print(f"Error: {e}")
