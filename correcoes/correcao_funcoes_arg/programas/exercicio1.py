'''
Utilizando o conceito de argumento (argv) em Python, escreva um programa que receba como argumentos uma opção (1 a 3) e mais 2 argumentos (números inteiros). O programa deverá ter uma função para checar e retornar qual é o menor número (opção 1), uma função para calcular a multiplicação desses números (opção 2) e outra para exibir todos os números dentro do intervalo definido pelos 2 argumentos numéricos (opção 3), desde que o primeiro número seja maior do que o segundo. OBS: o programa deve ter, obrigatoriamente, a função “main”.
'''
import sys

def main():
    lista_argumentos = sys.argv
    if (len(lista_argumentos) == 4):
        opcao = int(lista_argumentos[1])
        num1 = int(lista_argumentos[2])
        num2 = int(lista_argumentos[3])
        if (opcao >= 1 and opcao <= 3):
            match opcao:
                case 1:
                    print(f"O menor numero eh {retornar_menor(num1,num2)}")
                case 2:
                    print(f"O resultado da multiplicacao eh {calcular_multiplicacao(num1,num2)}")
                case 3:
                    exibir_numeros_intervalo(num1,num2)
        else:
            print("Opcao invalida!")
    else:
        print("Numero de argumentos invalido!")

def retornar_menor(num1,num2):
    if (num1 < num2):
        return(num1)
    else:
        return(num2)

def calcular_multiplicacao(num1,num2):
    mult = num1 * num2
    return(mult)

def exibir_numeros_intervalo(num1,num2):
    if (num1 < num2):
        for i in range(num1,num2+1):
            print(i)
    else:
        print("O primeiro numero deve ser menor que o segundo")

if (__name__ == "__main__"):
    main()