

def main():
    lista_valores = [300.00, 150.00, 830.00, 1200.00, 2500.00]


    # Sem MAP
    lista_valores_bf = []
    for i in range(5):
        valor_bf = calcular_desconto(lista_valores[i])
        lista_valores_bf.append(valor_bf)
    print(lista_valores_bf)

    # Com MAP
    lista_valores_bf = list(map(calcular_desconto, lista_valores))

def calcular_desconto(valor):
    valor_desconto = valor * 0.8
    return valor_desconto

if __name__ == '__main__':
    main()