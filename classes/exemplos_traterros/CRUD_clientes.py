def main():
    lista_clientes = []
    resp = 1
    while (resp == 1):
        print("1-Inserir cliente")
        print("2-Alterar cliente")
        print("3-Excluir cliente")
        print("4-Exibir clientes")
        print("5-Clientes com limite de crédito inferior a R$5000,00")
        print("6-Clientes cuja idade esteja entre 25 e 45 anos, com limite de crédito superior a R$2000")
        opcao = int(input("Digite a opcao desejada (1 a 6): "))
        if (opcao >= 1 and opcao <= 6):
            match opcao:
                case 1:
                    inserir_cliente(lista_clientes)
                case 2:
                    codigo = int(input("Digite o codigo do cliente que deseja alterar: "))
                    indice = buscar_cliente(lista_clientes,codigo)
                    if (indice != -1): # codigo existe
                        alterar_cliente(lista_clientes, indice)
                    else:
                        print("Codigo inexistente")
                case 3:
                    codigo = int(input("Digite o codigo do cliente a ser excluido: "))
                    indice = buscar_cliente(lista_clientes, codigo)
                    if (indice != -1):  # codigo existe
                        excluir_cliente(lista_clientes, indice)
                    else:
                        print("Codigo inexistente")
                case 4:
                    exibir_clientes(lista_clientes)
                case 5:
                    exibir_clientes_limite_inferior_5000(lista_clientes)
                case 6:
                    exibir_clientes_idade_limitecred(lista_clientes)
        else:
            print("Opcao invalida")
        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))

def inserir_cliente(lista_clientes):
    try:
        codigo = int(input("Codigo: "))
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        idade = int(input("Idade: "))
        endereco = input("Endereco: ")
        limite_cred = float(input("Limite de credito: "))
    except ValueError:
        print("Digite somente numeros para o codigo, cpf, idade ou lim. credito")
    else:
        cliente = {
            'Codigo':codigo,
            'Nome':nome,
            'CPF':cpf,
            'Idade':idade,
            'Endereco':endereco,
            'Limite_credito':limite_cred
        }
        lista_clientes.append(cliente)
        print("Cliente cadastrado com sucesso! ")
    finally:
        print("Operacao finalizada")

def buscar_cliente(lista_clientes,codigo):
    indice = -1
    for i in range(len(lista_clientes)):
        if (lista_clientes[i]['Codigo'] == codigo):
            indice = i
    return(indice)

def alterar_cliente(lista_clientes,indice):
    try:
        print(f"Nome: {lista_clientes[indice]['Nome']}")
        nome = input("Novo nome: ")
        print(f"CPF: {lista_clientes[indice]['CPF']}")
        cpf = int(input("Novo CPF: "))
        print(f"Idade: {lista_clientes[indice]['Idade']}")
        idade = int(input("Nova Idade: "))
        print(f"Endereco: {lista_clientes[indice]['Endereco']}")
        endereco = input("Novo Endereco: ")
        print(f"Limite de credito: R${lista_clientes[indice]['Limite_credito']:.2f}")
        limite_cred = float(input("Limite de credito: "))
    except ValueError:
        print("Digite somente numeros para o cpf, idade ou lim. credito")
    else:
        lista_clientes[indice]['Nome'] = nome
        lista_clientes[indice]['CPF'] = cpf
        lista_clientes[indice]['Idade'] = idade
        lista_clientes[indice]['Endereco'] = endereco
        lista_clientes[indice]['Limite_credito'] = limite_cred
        print("Cliente alterado com sucesso! ")
    finally:
        print("Operacao finalizada")

def excluir_cliente(lista_clientes,indice):
    lista_clientes.pop(indice)
    print("Cliente excluido com sucesso! ")

def exibir_clientes(lista_clientes):
    for cliente in lista_clientes:
        for chave,valor in cliente.items():
            print(f"{chave}: {valor}")
        print("-------------------------------------")

# Clientes com limite de crédito inferior a R$5000,00
def exibir_clientes_limite_inferior_5000(lista_clientes):
    for cliente in lista_clientes:
        if (cliente['Limite_credito'] < 5000):
            for chave,valor in cliente.items():
                print(f"{chave}: {valor}")
            print("-------------------------------------")

# Clientes cuja idade esteja entre 25 e 45 anos, com limite de crédito superior a R$2000
def exibir_clientes_idade_limitecred(lista_clientes):
    for cliente in lista_clientes:
        if (cliente['Idade'] >= 25 and cliente['Idade'] <= 45 and cliente['Limite_credito'] > 2000):
            for chave,valor in cliente.items():
                print(f"{chave}: {valor}")
            print("-------------------------------------")

if (__name__ == "__main__"):
    main()


