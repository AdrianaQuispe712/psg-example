print("Tabla de Verdad - Sistema de Seguridad (Operador XOR)")
print("Tarjeta | Huella | Puerta Abierta")
print("--------+--------+---------------")

# Caso 1: Sin tarjeta, sin huella
tarjeta = False
huella = False
puerta = tarjeta ^ huella
print(f"{tarjeta:^7} | {huella:^7} | {puerta:^13}")

# Caso 2: Sin tarjeta, con huella
tarjeta = False
huella = True
puerta = tarjeta ^ huella
print(f"{tarjeta:^7} | {huella:^7} | {puerta:^13}")

# Caso 3: Con tarjeta, sin huella
tarjeta = True
huella = False
puerta = tarjeta ^ huella
print(f"{tarjeta:^7} | {huella:^7} | {puerta:^13}")

# Caso 4: Con tarjeta y con huella
tarjeta = True
huella = True
puerta = tarjeta ^ huella
print(f"{tarjeta:^7} | {huella:^7} | {puerta:^13}")