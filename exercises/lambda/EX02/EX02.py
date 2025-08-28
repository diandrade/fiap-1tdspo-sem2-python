# Utilize o lambda e map para gerar uma nova lista de caracteres a partir de uma lista
# com caracteres maiúsculos e minúsculos.
# Quando o caractere for minúsculo, altere-o para maiúsculo e vice versa.

def main():
    lista_caracteres = ['m', 'T', 'X', 'i', 'O', 'P']
    lista_caracteres2 = list(map(lambda carac : carac.lower() if carac.isupper() else carac.upper(), lista_caracteres))

    print(lista_caracteres2)

if __name__ == '__main__':
    main()

