def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
print("Lucas(0):", lucas(0))
print("Lucas(5):", lucas(5))

valor_absoluto = lambda x: x if x >= 0 else -x
print("Valor absoluto de -8:", valor_absoluto(-8))
print("Valor absoluto de 5:", valor_absoluto(5))