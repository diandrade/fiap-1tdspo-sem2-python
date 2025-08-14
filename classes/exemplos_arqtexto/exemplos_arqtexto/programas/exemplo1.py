# Manipulacao de Arquivos texto

# Abertura e leitura de um arquivo texto (produtos_livraria.txt)
with open("produtos_livraria.txt","r",encoding="utf-8") as arqLivraria:
    # obter uma linha do arquivo
    linha = arqLivraria.readline()
    print(linha)
    arqLivraria.close()

# Obter todas as linhas do arquivo texto
try:
    with open("produtos_livraria.txt","r",encoding="utf-8") as arqLivraria:
        # obter todas as linhas
        linhas = arqLivraria.readlines()
        print(linhas)
        arqLivraria.close()
except FileNotFoundError:
    print("O arquivo nao existe")

# Gravar texto em um arquivo texto que nao existe
with open("produtos_farmacia.txt","w",encoding="utf-8") as arqFarmacia:
    texto = "Neosaldina  100  12.00\n"
    arqFarmacia.write(texto)
    arqFarmacia.close()
    
# Gravar texto em arquivo texto no final (sem perder o conteudo que ja existia)
# modo de abertura: a (append)
with open("produtos_farmacia.txt","a",encoding="utf-8") as arqFarmacia:
    texto = "Doril  300  7.00\n"
    arqFarmacia.write(texto)
    arqFarmacia.close()



