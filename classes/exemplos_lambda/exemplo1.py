# Funções Lambda
from twisted.words.xish.domish import elementStream

def main():
    # Exemplo 1: Função Lambda que cálcula o cubo de um número

    calcular_cubo = lambda num: num ** 3
    print(f"O cubo do número é {calcular_cubo(8)}")

    # Exemplo 2: Função Lambda que some 4 a um valor caso ele seja par e subtraia 2 caso seja ímpar

    alterar_numero = lambda num: num + 4 if (num % 2 == 0) else num - 2
    print(f"O número alterado é {alterar_numero(8)}")

if __name__ == '__main__':
    main()