import numbers as np
import math


# Definindo os números reais
a = -6
b = 6
n = 1000000

soma = 0  # Inicializando a variável soma

# Calculando o deltax
deltax = (b - a) / n
print("O valor de deltax é:", deltax)


# Definindo a função f(x) math.fabs(x) poderia ser usado, no entanto x² sera sempre positivo
def f(x):
    return 2 * math.pow(36-math.pow(x,2),1/2)

# Definindo a função f(x)
for i in range(1, n+1):
    xi = a + i* deltax
    soma += f(xi)*deltax

# Exibindo o resultado
print("O resultado da integral é:", soma)