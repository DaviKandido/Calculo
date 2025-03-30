import numbers as np
import math

# Calculo de Area


# Definindo os números reais
a = 0
b = 3
n = 1000000

soma = 0  # Inicializando a variável soma

# Calculando o deltax
deltax = (b - a) / n
print("O valor de deltax é:", deltax)


# Definindo a função f(x) math.fabs(x) poderia ser usado, no entanto x² sera sempre positivo
def f(x):
    return 4 * math.pi * x * math.pow((9 - math.pow(x, 2)), 1/2)

# Definindo a função f(x)
for i in range(1, n+1):
    xi = a + i* deltax
    soma += f(xi)*deltax

# Calculando o resultado do volume
volume = soma / b - a

# Exibindo o resultado
print("O resultado da integral é:", volume)