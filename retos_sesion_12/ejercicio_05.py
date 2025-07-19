contactos = []
nombre = input("Nombre: ")
telefono = input("Teléfono: ")
nombre_valido = bool(nombre.strip())
telefono_valido = False
if telefono.startswith('+') and len(telefono) == 12:
    digitos = telefono[1:]  
    telefono_valido = True
    for c in digitos:
        if not ('0' <= c <= '9'):
            telefono_valido = False
            break
if nombre_valido and telefono_valido:
    contactos.append((nombre, telefono))
    print("Contacto guardado")
else:
    print("Datos incorrectos")
