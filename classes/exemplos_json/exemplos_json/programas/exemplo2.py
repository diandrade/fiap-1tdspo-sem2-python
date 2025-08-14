# Exemplo de exportacao de uma lista de dicionários para um arquivo .json

import json

lista_pessoas = []

for i in range(3):
    try:
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")
    except ValueError:
        print("Digite dados numericos para o CPF ou a idade!")
    else:
        pessoa = {
            'Nome':nome,
            'CPF':cpf,
            'Idade':idade,
            'Telefone':telefone
        }
        lista_pessoas.append(pessoa)
    finally:
        print("Operacao finalizada!")

# Exportar os dados da lista de dicionarios para um arquivo .json
nome_arq = input("Digite o nome do arquivo json (com extensao): ")

with open(nome_arq,"w",encoding="utf-8") as arqPessoas:
    json.dump(lista_pessoas,arqPessoas,ensure_ascii=False,indent="\n")