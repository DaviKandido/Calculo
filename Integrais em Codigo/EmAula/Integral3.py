import numbers as np
import math


# Definindo os números reais
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
n = int(input("Digite o valor de n: "))

soma = 0  # Inicializando a variável soma

# Calculando o deltax
deltax = (b - a) / n
print(f"O valor de deltax é: {deltax}")


# Definindo a função f(x)
def f(x):
    return 4 * x * math.pi * math.pow((16 - ((x-6)**2)), 1/2)

# Definindo a função f(x)
for i in range(1, n+1):
    xi = a +i* deltax
    soma += f(xi)*deltax

# Exibindo o resultado
print(f"O resultado da integral é: {soma}")