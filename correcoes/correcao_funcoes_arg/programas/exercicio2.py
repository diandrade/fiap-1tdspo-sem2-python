'''
Utilizando o conceito de argumento (argv) em Python, escreva um programa que receba como argumentos uma opção (1 a 3) e mais 1 argumento (tamanho da lista). O programa deverá ter uma função para carregar os elementos da lista original de acordo com o tamanho que deve ser passado como argumento (opção 1), uma função para criar e exibir outra lista com o triplo dos elementos da lista original (opção 2) e outra para exibir somente os elementos pares da lista original (opção 3). OBS: o programa deve ter, obrigatoriamente, a função “main”.
'''
import sys

def main():
    lista_argumentos = sys.argv
    if (len(lista_argumentos) == 3):
        opcao = int(lista_argumentos[1])
        tam = int(lista_argumentos[2])
        if (opcao >= 1 and opcao <= 3):
            match opcao:
                case 1:
                    lista = []
                    inserir_lista(lista, tam)
                    print(lista)
                case 2:
                    lista = []
                    inserir_lista(lista, tam)
                    criar_lista_triplo(lista)
                case 3:
                    lista = []
                    inserir_lista(lista, tam)
                    exibir_pares(lista)
        else:
            print("Opcao invalida!")
    else:
        print("Numero de argumentos invalido!")


def inserir_lista(lista,tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

def criar_lista_triplo(lista):
    lista_triplo = []
    for i in range(len(lista)):
        lista_triplo.append(lista[i] * 3)
    print(lista_triplo)

def exibir_pares(lista):
    for i in range(len(lista)):
        if (lista[i] % 2 == 0):
            print(lista[i])

if (__name__ == "__main__"):
    main()