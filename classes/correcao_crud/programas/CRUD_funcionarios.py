'''
Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados: 

Código 

Nome do funcionário 

Idade do funcionário 

Salário do funcionário 

As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). 

OBS: o programa deverá ter, obrigatoriamente, a função “main” e cada operação do CRUD deverá ser uma função. Além das 4 funções do CRUD, acrescente a função para exibir todos os funcionários, bem como os seguintes relatórios: 

- Funcionários com idade superior a 25 anos; 

- Funcionários com idade entre 22 e 35 anos, cujo salário seja maior do que R$3700,00. 

Acrescente ao menu as opções para exportar os 3 relatórios para arquivos texto.

Acrescente ao menu as opções para exportar para um arquivo json e importar o json para uma lista de dicionários.

Incorpore ao CRUD o tratamento de erros (try...except...else...finally) nas operações de inserção e alteração.
'''
import json

def main():
    lista_funcionarios = []
    resp = 1

    while (resp == 1):
        print("1-Inserir funcionario")
        print("2-Alterar funcionario")
        print("3-Excluir funcionario")
        print("4-Exibir dados de um funcionario")
        print("5-Exibir dados de todos os funcionarios")
        print("6-Exibir funcionários com idade superior a 25 anos")
        print("7-Exibir funcionários com idade entre 22 e 35 anos, cujo salário seja maior do que R$3700,00")
        print("8-Exportar dados de todos os funcionarios para um arquivo texto")
        print("9-Exportar o relatório dos funcionários com idade superior a 25 anos para um arquivo texto")
        print("10-Exportar o relatório dos funcionários com idade entre 22 e 35 anos, cujo salário seja maior do que R$3700,00 para um arquivo texto")
        print("11-Exportar dados para um arquivo json")
        print("12-Importar dados de um arquivo json para a tabela")
        opcao = int(input("Digite a opcao desejada (1 a 12): "))
        if (opcao >= 1 and opcao <= 12):
            match opcao:
                case 1:
                    inserir_funcionario(lista_funcionarios)
                case 2:
                    cod_alterar = int(input("Digite o codigo do funcionario que deseja alterar: "))
                    indice = buscar_funcionario(lista_funcionarios,cod_alterar)
                    if (indice != -1):
                        alterar_funcionario(lista_funcionarios,indice)
                    else:
                        print("Codigo inexistente!")
                case 3:
                    cod_excluir = int(input("Digite o codigo do funcionario que deseja excluir: "))
                    indice = buscar_funcionario(lista_funcionarios, cod_excluir)
                    if (indice != -1):
                        excluir_funcionario(lista_funcionarios, indice)
                    else:
                        print("Codigo inexistente!")
                case 4:
                    cod_exibir = int(input("Digite o codigo do funcionario que deseja exibir: "))
                    exibir_dados_funcionario(lista_funcionarios,cod_exibir)
                case 5:
                    exibir_exportar_funcionarios(lista_funcionarios,1) # 1-exibir / 2-exportar
                case 6:
                    exibir_exportar_relatorio1(lista_funcionarios,1) # 1-exibir / 2-exportar
                case 7:
                    exibir_exportar_relatorio2(lista_funcionarios,1) # 1-exibir / 2-exportar
                case 8:
                    exibir_exportar_funcionarios(lista_funcionarios,2)
                case 9:
                    exibir_exportar_relatorio1(lista_funcionarios,2)
                case 10:
                    exibir_exportar_relatorio2(lista_funcionarios,2)
                case 11:
                    exportar_funcionarios_json(lista_funcionarios)
                case 12:
                    importar_funcionarios_tabela(lista_funcionarios)
        else:
            print("Opcao invalida!")
        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))

# Funcoes
def buscar_funcionario(lista_funcionarios,cod):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Codigo'] == cod):
            indice = i
    return(indice)

def inserir_funcionario(lista_funcionarios):
    try:
        codigo = int(input("Digite o codigo do funcionario: "))
        indice = buscar_funcionario(lista_funcionarios,codigo)
        while (indice != -1): # quer dizer que o codigo ja existe
            codigo = int(input("Esse codigo ja existe! Digite outro codigo: "))
            indice = buscar_funcionario(lista_funcionarios, codigo)
        # inputs dos outros dados
        nome = input("Digite o nome do funcionario: ")
        idade = int(input("Digite a idade do funcionario: "))
        salario = float(input("Digite o salario do funcionario: "))
    except ValueError:
        print("Digite dados numericos para o codigo, idade ou salario!")
    else:
        funcionario = {
            'Codigo':codigo,
            'Nome':nome,
            'Idade':idade,
            'Salario':salario
        }
        lista_funcionarios.append(funcionario)
        print("Funcionario incluido com sucesso!")
    finally:
        print("Operacao finalizada! \n")

def alterar_funcionario(lista_funcionarios,indice):
    try:
        print(f"Nome: {lista_funcionarios[indice]['Nome']}")
        novo_nome = input("Digite o novo nome: ")
        print(f"Idade: {lista_funcionarios[indice]['Idade']}")
        nova_idade = int(input("Digite a nova idade: "))
        print(f"Salario: {lista_funcionarios[indice]['Salario']}")
        novo_salario = float(input("Digite o novo salario: "))
    except ValueError:
        print("Digite dados numericos para a idade ou salario!")
    else:
        lista_funcionarios[indice]['Nome'] = novo_nome
        lista_funcionarios[indice]['Idade'] = nova_idade
        lista_funcionarios[indice]['Salario'] = novo_salario
        print("Funcionario alterado com sucesso!")
    finally:
        print("Operacao finalizada \n")

def excluir_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Funcionario excluido com sucesso! \n")

def exibir_dados_funcionario(lista_funcionarios,cod):
    indice = buscar_funcionario(lista_funcionarios,cod)
    if (indice != -1):
        for chave,valor in lista_funcionarios[indice].items():
            print(f"{chave}: {valor}")
    else:
        print("Codigo inexistente! \n")

def exibir_exportar_funcionarios(lista_funcionarios,opcao):
    if (len(lista_funcionarios) > 0):
        if (opcao == 1): # exibir
            for funcionario in lista_funcionarios:
                for chave, valor in funcionario.items():
                    print(f"{chave}: {valor}")
                print("------------------------------------")
        else: # exportar para o txt
            nome_arq = input("Digite o nome do arquivo texto (com extensao): ")
            for funcionario in lista_funcionarios:
                texto_dados = str(funcionario['Codigo']) + "\t" + funcionario['Nome'] + "\t" + str(funcionario['Idade']) + "\t" + str(funcionario['Salario']) + "\n"
                with open(nome_arq,"a",encoding="utf-8") as arqFuncionarios:
                    arqFuncionarios.write(texto_dados)
                    arqFuncionarios.close()
            print("Arquivo txt gerado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def exibir_exportar_relatorio1(lista_funcionarios,opcao):
    if (len(lista_funcionarios) > 0):
        if (opcao == 1): # exibir
            for funcionario in lista_funcionarios:
                if (funcionario['Idade'] > 25):
                    for chave, valor in funcionario.items():
                        print(f"{chave}: {valor}")
                    print("------------------------------------")
        else: # exportar para o txt
            nome_arq = input("Digite o nome do arquivo texto (com extensao): ")
            for funcionario in lista_funcionarios:
                if (funcionario['Idade'] > 25):
                    texto_dados = str(funcionario['Codigo']) + "\t" + funcionario['Nome'] + "\t" + str(funcionario['Idade']) + "\t" + str(funcionario['Salario']) + "\n"
                    with open(nome_arq,"a",encoding="utf-8") as arqFuncionarios:
                        arqFuncionarios.write(texto_dados)
                        arqFuncionarios.close()
            print("Arquivo txt gerado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def exibir_exportar_relatorio2(lista_funcionarios,opcao):
    if (len(lista_funcionarios) > 0):
        if (opcao == 1): # exibir
            for funcionario in lista_funcionarios:
                if (funcionario['Idade'] >= 22 and funcionario['Idade'] <= 35 and funcionario['Salario'] > 3700):
                    for chave, valor in funcionario.items():
                        print(f"{chave}: {valor}")
                    print("------------------------------------")
        else: # exportar para o txt
            nome_arq = input("Digite o nome do arquivo texto (com extensao): ")
            for funcionario in lista_funcionarios:
                if (funcionario['Idade'] >= 22 and funcionario['Idade'] <= 35 and funcionario['Salario'] > 3700):
                    texto_dados = str(funcionario['Codigo']) + "\t" + funcionario['Nome'] + "\t" + str(funcionario['Idade']) + "\t" + str(funcionario['Salario']) + "\n"
                    with open(nome_arq,"a",encoding="utf-8") as arqFuncionarios:
                        arqFuncionarios.write(texto_dados)
                        arqFuncionarios.close()
            print("Arquivo txt gerado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def exportar_funcionarios_json(lista_funcionarios):
    if (len(lista_funcionarios) > 0):
        nome_arq = input("Digite o nome do arquivo json: ")
        with open(nome_arq,"w",encoding="utf-8") as arqFuncionarios:
            json.dump(lista_funcionarios,arqFuncionarios,ensure_ascii=False,indent="\n")
            arqFuncionarios.close()
        print("Arquivo json gravado com sucesso! \n")
    else:
        print("Tabela vazia! \n")

def importar_funcionarios_tabela(lista_funcionarios):
    lista_funcionarios.clear()
    nome_arq = input("Digite o nome do arquivo json: ")
    with open(nome_arq,"r",encoding="utf-8") as arqFuncionarios:
        dados_arq = arqFuncionarios.read()
        lista_dados = json.loads(dados_arq)
        for dados_func in lista_dados:
            lista_funcionarios.append(dados_func)
        arqFuncionarios.close()
    print("Dados importados com sucesso! \n")

if (__name__ == "__main__"):
    main()

