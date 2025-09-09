'''
Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:  

Código  

Descrição do produto  

Quantidade em estoque  

Valor do produto  

As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).  

OBS: o programa deverá ter, obrigatoriamente, a função “main” e cada operação do CRUD deverá ser uma função. Além das 4 funções do CRUD, acrescente a função para exibir todos os funcionários, bem como os seguintes relatórios:  

- Produtos cujo valor esteja entre R$150,00 e R$500,00;  

- Produtos com quantidade superior a 100 unidades.  

Acrescente ao menu as opções para exportar os 3 relatórios para arquivos texto. 

Acrescente ao menu as opções para exportar para um arquivo json e importar o json para uma lista de dicionários. 

 

Incorpore ao CRUD o tratamento de erros (try...except...else...finally) nas operações de inserção e alteração. 
'''
import json

def main():
    lista_produtos = []
    resp = 1

    while (resp == 1):
        print("1-Inserir produto")
        print("2-Alterar produto")
        print("3-Excluir produto")
        print("4-Exibir dados de um produto")
        print("5-Exibir dados de todos os produtos")
        print("6-Exibir os produtos cujo valor esteja entre R$150,00 e R$500,00")
        print("7-Exibir os produtos com quantidade superior a 100 unidades")
        print("8-Exportar dados de todos os produtos para um arquivo texto")
        print("9-Exportar o relatório dos produtos cujo valor esteja entre R$150,00 e R$500,00 para um arquivo texto")
        print("10-Exportar o relatório dos produtos com quantidade superior a 100 unidades para um arquivo texto")
        print("11-Exportar dados para um arquivo json")
        print("12-Importar dados de um arquivo json para a tabela")
        opcao = int(input("Digite a opcao desejada (1 a 12): "))
        if (opcao >= 1 and opcao <= 12):
            match opcao:
                case 1:
                    inserir_produto(lista_produtos)
                case 2:
                    cod_alterar = int(input("Digite o codigo do produto que deseja alterar: "))
                    indice = buscar_produto(lista_produtos,cod_alterar)
                    if (indice != -1):
                        alterar_produto(lista_produtos,indice)
                    else:
                        print("Codigo inexistente!")
                case 3:
                    cod_excluir = int(input("Digite o codigo do produto que deseja excluir: "))
                    indice = buscar_produto(lista_produtos, cod_excluir)
                    if (indice != -1):
                        excluir_produto(lista_produtos, indice)
                    else:
                        print("Codigo inexistente!")
                case 4:
                    cod_exibir = int(input("Digite o codigo do produto que deseja exibir: "))
                    exibir_dados_produto(lista_produtos,cod_exibir)
                case 5:
                    exibir_exportar_produtos(lista_produtos,1) # 1-exibir / 2-exportar
                case 6:
                    exibir_exportar_relatorio1(lista_produtos,1) # 1-exibir / 2-exportar
                case 7:
                    exibir_exportar_relatorio2(lista_produtos,1) # 1-exibir / 2-exportar
                case 8:
                    exibir_exportar_produtos(lista_produtos,2)
                case 9:
                    exibir_exportar_relatorio1(lista_produtos,2)
                case 10:
                    exibir_exportar_relatorio2(lista_produtos,2)
                case 11:
                    exportar_produtos_json(lista_produtos)
                case 12:
                    importar_produtos_tabela(lista_produtos)
        else:
            print("Opcao invalida!")
        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))

# Funcoes
def buscar_produto(lista_produtos,cod):
    indice = -1
    for i in range(len(lista_produtos)):
        if (lista_produtos[i]['Codigo'] == cod):
            indice = i
    return(indice)

def inserir_produto(lista_produtos):
    try:
        codigo = int(input("Digite o codigo do produto: "))
        indice = buscar_produto(lista_produtos,codigo)
        while (indice != -1): # quer dizer que o codigo ja existe
            codigo = int(input("Esse codigo ja existe! Digite outro codigo: "))
            indice = buscar_produto(lista_produtos, codigo)
        # inputs dos outros dados
        nome = input("Digite o nome do produto: ")
        idade = int(input("Digite a idade do produto: "))
        salario = float(input("Digite o salario do produto: "))
    except ValueError:
        print("Digite dados numericos para o codigo, idade ou salario!")
    else:
        produto = {
            'Codigo':codigo,
            'Nome':nome,
            'Idade':idade,
            'Salario':salario
        }
        lista_produtos.append(produto)
        print("produto incluido com sucesso!")
    finally:
        print("Operacao finalizada! \n")

def alterar_produto(lista_produtos,indice):
    try:
        print(f"Nome: {lista_produtos[indice]['Nome']}")
        novo_nome = input("Digite o novo nome: ")
        print(f"Idade: {lista_produtos[indice]['Idade']}")
        nova_idade = int(input("Digite a nova idade: "))
        print(f"Salario: {lista_produtos[indice]['Salario']}")
        novo_salario = float(input("Digite o novo salario: "))
    except ValueError:
        print("Digite dados numericos para a idade ou salario!")
    else:
        lista_produtos[indice]['Nome'] = novo_nome
        lista_produtos[indice]['Idade'] = nova_idade
        lista_produtos[indice]['Salario'] = novo_salario
        print("produto alterado com sucesso!")
    finally:
        print("Operacao finalizada \n")

def excluir_produto(lista_produtos,indice):
    lista_produtos.pop(indice)
    print("produto excluido com sucesso! \n")

def exibir_dados_produto(lista_produtos,cod):
    indice = buscar_produto(lista_produtos,cod)
    if (indice != -1):
        for chave,valor in lista_produtos[indice].items():
            print(f"{chave}: {valor}")
    else:
        print("Codigo inexistente! \n")

def exibir_exportar_produtos(lista_produtos,opcao):
    if (len(lista_produtos) > 0):
        if (opcao == 1): # exibir
            for produto in lista_produtos:
                for chave, valor in produto.items():
                    print(f"{chave}: {valor}")
                print("------------------------------------")
        else: # exportar para o txt
            nome_arq = input("Digite o nome do arquivo texto (com extensao): ")
            for produto in lista_produtos:
                texto_dados = str(produto['Codigo']) + "\t" + produto['Nome'] + "\t" + str(produto['Idade']) + "\t" + str(produto['Salario']) + "\n"
                with open(nome_arq,"a",encoding="utf-8") as arqprodutos:
                    arqprodutos.write(texto_dados)
                    arqprodutos.close()
            print("Arquivo txt gerado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def exibir_exportar_relatorio1(lista_produtos,opcao):
    if (len(lista_produtos) > 0):
        if (opcao == 1): # exibir
            for produto in lista_produtos:
                if (produto['Idade'] > 25):
                    for chave, valor in produto.items():
                        print(f"{chave}: {valor}")
                    print("------------------------------------")
        else: # exportar para o txt
            nome_arq = input("Digite o nome do arquivo texto (com extensao): ")
            for produto in lista_produtos:
                if (produto['Idade'] > 25):
                    texto_dados = str(produto['Codigo']) + "\t" + produto['Nome'] + "\t" + str(produto['Idade']) + "\t" + str(produto['Salario']) + "\n"
                    with open(nome_arq,"a",encoding="utf-8") as arqprodutos:
                        arqprodutos.write(texto_dados)
                        arqprodutos.close()
            print("Arquivo txt gerado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def exibir_exportar_relatorio2(lista_produtos,opcao):
    if (len(lista_produtos) > 0):
        if (opcao == 1): # exibir
            for produto in lista_produtos:
                if (produto['Idade'] >= 22 and produto['Idade'] <= 35 and produto['Salario'] > 3700):
                    for chave, valor in produto.items():
                        print(f"{chave}: {valor}")
                    print("------------------------------------")
        else: # exportar para o txt
            nome_arq = input("Digite o nome do arquivo texto (com extensao): ")
            for produto in lista_produtos:
                if (produto['Idade'] >= 22 and produto['Idade'] <= 35 and produto['Salario'] > 3700):
                    texto_dados = str(produto['Codigo']) + "\t" + produto['Nome'] + "\t" + str(produto['Idade']) + "\t" + str(produto['Salario']) + "\n"
                    with open(nome_arq,"a",encoding="utf-8") as arqprodutos:
                        arqprodutos.write(texto_dados)
                        arqprodutos.close()
            print("Arquivo txt gerado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def exportar_produtos_json(lista_produtos):
    if (len(lista_produtos) > 0):
        nome_arq = input("Digite o nome do arquivo json: ")
        with open(nome_arq,"w",encoding="utf-8") as arqprodutos:
            json.dump(lista_produtos,arqprodutos,ensure_ascii=False,indent="\n")
            arqprodutos.close()
        print("Arquivo json gravado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def importar_produtos_tabela(lista_produtos):
    lista_produtos.clear()
    nome_arq = input("Digite o nome do arquivo json: ")
    with open(nome_arq,"r",encoding="utf-8") as arqprodutos:
        dados_arq = arqprodutos.read()
        lista_dados = json.loads(dados_arq)
        for dados_func in lista_dados:
            lista_produtos.append(dados_func)
        arqprodutos.close()
    print("Dados importados com sucesso! \n")

if (__name__ == "__main__"):
    main()