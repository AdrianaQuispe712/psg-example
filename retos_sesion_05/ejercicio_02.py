# Conviert
def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

temperaturas_f = [25, 300, 76]
for f in temperaturas_f:
    c = fahrenheit_a_celsius(f)
    print(f"{f} °F = {c:.2f} °C")
