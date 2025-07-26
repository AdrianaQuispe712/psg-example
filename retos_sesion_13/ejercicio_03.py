print("\nEjercicio 3 Felicitaciones a aprobados")
estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]
for estudiante in estudiantes:
    nombre = estudiante[0]
    nota = estudiante[1]
    if nota >= 51:
        print(f"Felicidades {nombre}, aprobaste con {nota} puntos.")
