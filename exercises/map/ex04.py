def main():
    lista_palavras = ["FIAP", "TDS", "Daniel", "Python", "João"]
    lista_minusculo = list(map(converter_minusculo, lista_palavras))
    print(lista_minusculo)

def converter_minusculo(palavra):
    return palavra.lower()

if __name__ == '__main__':
    main()