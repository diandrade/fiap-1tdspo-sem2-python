def main():
    listaOriginal = [234, 64, 13467, 45.89, 23]
    listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]
    lista_descontos = list(map(aplicar_desconto, listaOriginal, listaDescontos))
    print(lista_descontos)

def aplicar_desconto(valor, desc):
    valor_desc = valor * (1 - desc)
    return (valor_desc)

if __name__ == '__main__':
    main()