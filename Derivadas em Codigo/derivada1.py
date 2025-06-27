import numbers as num
import math as math

    
def derivadaEmX(x, y):
    return 12*(x**5)-156*(x**3)+432*x

def derivadaEmY(x, y):
    return (y**6)+2*(y**5)-101*(y**4)+100*(y**2)+(200*y)-202*(y**3)

def derivadaEmXX(x, y):
    return 60*(x**4)-468*(x**2)+432

def derivadaEmXY(x, y):
    return 0

def derivadaEmYY(x, y):
    return 6*(y**5)+10*(y**4)-404*(y**3)+200*(y)+200-606*(y**2)


def calcularPontos(x, y):
    print("A derivada em xX é: ", derivadaEmXX(x, y))
    print("A derivada em xY é: ", derivadaEmXY(x, y))
    print("A derivada em yY é: ", derivadaEmYY(x, y))

    D = derivadaEmXX(x, y)*derivadaEmYY(x, y) - (derivadaEmXY(x, y)**2)
    print("O valor de D e: ", D)

    match D:
        case d if d > 0:
            if derivadaEmXX(x, y) > 0:
                print("Ponto de mínimo local")
            else:
                print("Ponto de máximo local")
        case d if d < 0:
            print("-> Ponto de sela")
        case _:
            print("Teste inconclusivo")
    print("-----------------------------------------------------------------")

def ler_Arquivo(arquivo):
    with open(arquivo, "r") as f:  # Abre o arquivo em modo de leitura
        conteudo = f.readlines()  # Leitura das linhas do arquivo
        return conteudo 

def main():
    # x = float(input("Digite o valor de x: "))
    # y = float(input("Digite o valor de y: "))
    x = 0
    y = 0
    conteudo = ler_Arquivo("combinacoes_xy.txt")
    for i in conteudo:
        conteudoTratado = i.replace("\n", "").split(" ")
        x = float(conteudoTratado[0])
        y = float(conteudoTratado[1])

        print("A derivada em x é: ", derivadaEmX(x, y))
        print("A derivada em y é: ", derivadaEmY(x, y))

        if (derivadaEmX(x,y) == 0 and derivadaEmY(x,y) == 0):
            print("-> Logo é um ponto crítico\n")
            calcularPontos(x, y)
        else:
            print("-> Logo nao é um ponto crítico\n")



if __name__ == "__main__":
    main()