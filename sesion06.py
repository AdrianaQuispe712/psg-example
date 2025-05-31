# # Verificar si el número está en el rango usando operadores lógicos
# if 20 >= 0 and 20 <= 100:
#     print(f"El número {20} está en el rango de 0 a 100")
# else:
#     print(f"El número {20} NO está en el rango de 0 a 100")
    
    
    
    

# notas = [15, 20, 16]
# suma_notas = sum(notas)
# aprobado = suma_notas > 50
# print(f"Suma total de notas: {suma_notas}")
# print(f"Aprobo con nota superior a 50? {aprobado}")




numero = 15
resul = (numero % 3 == 0) and (numero % 5 == 0) and (numero % 2 != 0)
print(resul)  # true o false