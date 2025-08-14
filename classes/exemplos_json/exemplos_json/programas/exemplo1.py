# Manipulacao de arquivos .json

import json

with open("alunos_idade.json","r",encoding="utf-8") as arqAlunos:
    dados_arq = arqAlunos.read()
    listaAlunos = json.loads(dados_arq)
    print(listaAlunos)
    print(f"Dados do segundo aluno: {listaAlunos[1]}")
    print(f"Idade do terceiro aluno: {listaAlunos[2]['idade']}")

# Leitura do arquivo .json
with open("log.json","r",encoding="utf-8") as arqLog:
    dados_arq = arqLog.read()
    listaLogs = json.loads(dados_arq)
    print(f"Tabela do primeiro evento do log: {listaLogs[0]['tableName']}")
    print(f"Primeira chave do fields: {listaLogs[0]['fields']['1']}")