print("Ejercicio 1 Sucesión de Lucas")
a = 2
b = 1
for i in range(20):
    print(a, end=" ")
    siguiente = a + b
    a = b
    b = siguiente
