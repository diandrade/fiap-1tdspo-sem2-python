import sys

lista = []
lista_triplo = []

import sys

def main():
    lista_argumentos = sys.argv
    if len(lista_argumentos) == 3:
        opcao = int(lista_argumentos[1])
        tam = int(lista_argumentos[2])
        if 1 <= opcao <= 3:
            match opcao:
                case 1:
                    lista = []
                    inserir_lista(lista, tam)
                    print(lista)
                case 2:
                    lista = []
                    inserir_lista(lista, tam)
                    criar_lisa_triplo(lista)
                case 3:
                    lista = []
                    inserir_lista(lista, tam)
                    exibir_pares(lista)
        else:
            print("Opção Inválida.")
    else:
        print("Número de argumento inválido.")
def inserir_lista(lista, tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

def criar_lisa_triplo(lista):
    lista_triplo = []
    for i in range(len(lista)):
        lista_triplo.append(lista[i] * 3)
    print(lista_triplo)

def exibir_pares(lista):
    for i in range(len(lista)):
        if (lista[i] % 2 == 0):
            print(lista[i])

if __name__ == '__main__':
    main()