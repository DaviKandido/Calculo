import math

# Limites da integral
a = 0.0
b = math.pi /4
n = 1000000  # Reduzi para 1 milhão que já é suficiente

deltax = (b - a) / n
soma = 0.0

# Função CORRETA agora (usando log natural)
def f(x):
    return (9 * (math.sin(x) ** 3) * (math.cos(x) ** 3)) + (12 * math.tan

# Método do trapézio
soma = (f(a) + f(b)) / 2
for i in range(1, n):
    xi = a + i * deltax
    soma += f(xi)

soma *= deltax

print("Volume calculado:", soma)