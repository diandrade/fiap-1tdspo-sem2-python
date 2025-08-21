def main():
    lista_numeros = [9, 4, 6, 3, 10]
    nova_lista = list(map(alterar_numero, lista_numeros))
    print(nova_lista)

def alterar_numero(num):
    if num % 2 == 0:
        return num + 5
    else:
        return num - 2

if __name__ == '__main__':
    main()
