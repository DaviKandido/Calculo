import numbers as np
import math


# Definindo os números reais
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
n = int(input("Digite o valor de n: "))

soma = 0  # Inicializando a variável soma

# Calculando o deltax
deltax = (b - a) / n
print("O valor de deltax é:", deltax)


# Definindo a função f(x)
def f(x):
    return math.sin(x) * math.cos(x)  # Exemplo de função, você pode alterar conforme necessário

# Definindo a função f(x)
for i in range(1, n+1):
    xi = a + i* deltax
    # fx = xi * f(xi)
    soma += f(xi)*deltax

# Exibindo o resultado
print("O resultado da integral é:", soma)