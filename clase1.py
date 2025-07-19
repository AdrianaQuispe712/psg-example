#pedir un  numero entero en dias y mostrar su equivalente en minutos,segundo, semanas, y anios(Extra de meses)
dias = int(input("Introduce los dias:"))
segundos = dias*(24/dias)*(60/1)*(60/1)
print(f"Los {dias} días en segundos son: {segundos}")

# minutos= 

# semanas= 

anios= dias*(1/365)
print(f"Los {dias} dias en anio es: {anios}")