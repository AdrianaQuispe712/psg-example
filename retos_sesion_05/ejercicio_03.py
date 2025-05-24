segundos_totales = 1000000

semanas = segundos_totales // (7 * 24 * 3600)
resto = segundos_totales % (7 * 24 * 3600)

dias = resto // (24 * 3600)
resto %= (24 * 3600)

horas = resto // 3600
resto %= 3600

minutos = resto // 60
segundos = resto % 60

print(f"{segundos_totales} segundos = {semanas} semanas {dias} días {horas} horas {minutos} minutos {segundos} segundos")
