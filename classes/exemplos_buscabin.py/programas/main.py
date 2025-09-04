def main():
    lista = []
    inserir_lista(lista, 10)
    ordenar_bubble_sort(lista)
    print(lista)
    elem = int(input("Digite o elemento que deseja procurar: "))
    indice = busca_binaria(lista, elem)
    if (indice != -1):
        print(f"O elemento está no índice {indice} da lista")
    else:
        print("O elemento não está na lista")

def busca_binaria(lista, elem):
    ini = 0
    fim = len(lista) - 1
    while (ini <= fim):
        meio = (ini + fim)//2
        if (elem == lista[meio]): #Encontrou o Elemento
            return (meio)
        else:
            if (elem < lista[meio]):
                fim = meio - 1
            else:
                ini = meio + 1

    return (-1)

def ordenar_bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1, 0, -1):
        for j in range(0,i):
            if (lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

def inserir_lista(lista,tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

if __name__ == '__main__':
    main()