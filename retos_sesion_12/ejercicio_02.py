# Diccionario con usuarios y contraseñas
usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")

if usuario in usuarios and usuarios[usuario] == contrasena:
    print("Acceso Aprobado")
else:
    print("Acceso Denegado")
