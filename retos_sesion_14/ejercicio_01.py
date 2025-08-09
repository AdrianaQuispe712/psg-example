def L_Calificacion(listadeCal):
    cont=0;
    sum=0;
    for i in listadeCal:
        cont = cont +  1
        sum = sum + i
    promedio = sum / cont
    return promedio
      
Calificacion = [50,75,80,91,70]
Resultado = L_Calificacion(Calificacion)
print(Resultado)










