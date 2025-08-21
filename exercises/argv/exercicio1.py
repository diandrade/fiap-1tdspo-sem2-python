import sys

def main():
    lista_argumentos = sys.argv
    if len(lista_argumentos) == 4:
        opcao = int(lista_argumentos[1])
        num1 = int(lista_argumentos[2])
        num2 = int(lista_argumentos[3])
        if 1 <= opcao <= 3:
            match opcao:
                case 1:
                    print(f"O menor número é {retornar_menor(num1, num2)}")
                case 2:
                    print(f"O resultado da multiplicação é {calcular_multiplicacao(num1,num2)}")
                case 3:
                    exibir_numeros_intervalo(num1,num2)
        else:
            print("Opção inválida!")
    else:
        print("Número de argumentos inválido!")

def retornar_menor (num1, num2):
    if (num1 < num2):
        return (num1)
    else:
        return (num2)

def calcular_multiplicacao(num1,num2):
    mult = num1 * num2
    return (mult)

def exibir_numeros_intervalo(num1,num2):
    if(num1 < num2):
        for i in range(num1, num2 + 1):
            print(i)
    else:
        print("O primeiro número deve ser menor que o segundo.")

if __name__ == '__main__':
    main()


