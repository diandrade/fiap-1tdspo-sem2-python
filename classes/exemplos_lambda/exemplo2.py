# Combinação do Lambda com MAP

# Exemplo: Calcular o IPVA baseado na lista de valores e na lista de idades dos veículos

lista_valores = [85000, 120000, 25000, 15000, 300000]
lista_idades = [3, 2, 22, 27, 1]

lista_ipvas = list(map(lambda valor, idade : valor * 0.04 if (idade < 20) else 0, lista_valores, lista_idades))

print(lista_ipvas)