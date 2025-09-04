def main():
    lista = []

    inserir_lista(lista, 10)

    ordenar_bubble_sort(lista)

    print(lista)

def inserir_lista(lista,tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

# metodo de Ordenacao Bubble Sort
def ordenar_bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1, 0, -1):
        for j in range(0,i):
            if (lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

if (__name__ == "__main__"):
    main()