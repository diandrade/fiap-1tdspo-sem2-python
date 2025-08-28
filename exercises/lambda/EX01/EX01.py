# Utilizando os conceitos de funções lambda e Map, calcule o somatório dos valores pares e ímpares de uma lista. DICA:
# deverão ser geradas duas listas (uma para os pares e outra para os ímpares) para fazer as somas.
# Para tanto, utilize a função SUM.

# # Funções Lambda
# from twisted.words.xish.domish import elementStream
#
# def main():
#     # Exemplo 1: Função Lambda que cálcula o cubo de um número
#
#     calcular_cubo = lambda num: num ** 3
#     print(f"O cubo do número é {calcular_cubo(8)}")
#
#     # Exemplo 2: Função Lambda que some 4 a um valor caso ele seja par e subtraia 2 caso seja ímpar
#
#     alterar_numero = lambda num: num + 4 if (num % 2 == 0) else num - 2
#     print(f"O número alterado é {alterar_numero(8)}")
#
# if __name__ == '__main__':
#     main()

def sem_usar_lambda():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    impares = []
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    for impar in impares:
        print(impar)

    print("-" * 50)

    for par in pares:
        print(par)

def usando_lambda():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    impares = []
    pares = []

    list(map(lambda numero : pares.append(numero) if numero % 2 == 0 else impares.append(numero), numeros))

    for impar in impares:
        print(impar)

    print("-" * 50)

    for par in pares:
        print(par)

def solucao_professor():
    lista_numeros = [6, 5, 4, 3, 2, 1]

    soma_pares = sum(list(map(lambda num : num if (num % 2 == 0) else 0, lista_numeros)))
    soma_impares = sum(list(map(lambda num: num if (num % 2 != 0) else 0, lista_numeros)))

    print(f"Soma dos Pares: {soma_pares}")
    print(f"Soma dos Impares: {soma_impares}")

def main():
      #sem_usar_lambda()
      usando_lambda()


if __name__ == '__main__':
    main()