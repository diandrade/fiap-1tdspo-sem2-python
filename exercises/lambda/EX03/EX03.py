# 3) Escreva um programa com a função “main”, o qual deverá ter a seguinte função:
# a. Uma função que receba duas listas como parâmetros (uma lista de preços e outra de quantidades de cada produto comprado),
# o valor do produto e a quantidade comprada. A função deverá inserir nas listas o valor comprado e a quantidade, respectivamente.
# O programa deverá solicitar ao usuário a quantidade do produto, bem como seu preço até que seja digitada
# uma opção para saída (por exemplo, 1-continuar e 0-sair). Na sequência, após a digitação dos produtos,
# utilizando conceitos da função lambda e map, crie uma nova lista com o valor total de cada item (quantidade x produto)
# e, por fim, calcule o valor total da compra.

def main():
    lista_precos = []
    lista_qtdes = []
    resp = 1
    while (resp == 1):
        preco = float(input("Preco: "))
        qtde = int(input("Quantidade: "))
        inserir_preco_qtde(lista_precos, lista_qtdes, preco, qtde)
        resp = int(input("Deseja continuar (1-SIM / 0-NÃO): "))

    total_venda = sum(list(map(lambda preco, qtde : qtde * preco, lista_precos, lista_qtdes)))

    print(f"Valor total da venda: R${total_venda:.2f}")

def inserir_preco_qtde(lista_preco, lista_qtde, preco, qtde):
    lista_preco.append(preco)
    lista_qtde.append(qtde)

if __name__ == '__main__':
    main()