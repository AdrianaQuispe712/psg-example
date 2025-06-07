# 1. endswith() – Verifica si termina con cierto texto
archivo = "reporte_final.txt"
print(archivo.endswith(".txt"))

# 2. zfill() – Rellenar con ceros a la izquierda
codigo = "23"
print(codigo.zfill(5))  # Resultado: '00023'

# 3. center() – Centra una cadena en un ancho específico
titulo = "Python"
print(titulo.center(20, "-"))

# 4. ljust() – Justifica a la izquierda
nombre = "Ana"
print(nombre.ljust(10, "."))  # Resultado: 'Ana.......'

# 5. partition() – Divide en una tupla en torno a un separador
mensaje = "Hola mundo bonito"
print(mensaje.partition("mundo "))  # ('Hola ', 'mundo', ' bonito')
#

#
..