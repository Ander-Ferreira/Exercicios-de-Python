#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
#Adição(+), subtração(-), multiplicação(*), ou divisão(/). Exiba na tela o resultado da operação desejada.

print('Calculadora Simples')
print('Adição "+", Subtração "-", Multiplicação "*", Divisão "/"')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite mais um número: '))
sinal = input('Digite o sinal de sua operação: ')

if(sinal == '+'):
    adicao = num1 + num1
    print(f'O resultado da adição é: {adicao}')

elif(sinal == "-"):
    sub = num1 - num2
    print(f'O resultado da subtração é: {sub}')

elif(sinal == "*"):
    multi = num1 * num2
    print(f'O resultado da multiplicação é: {multi} ')

elif(sinal == "/"):
    divisao = num1 / num2
    print(f'O resultado da divisão é: {divisao}')

else:
    print('Operação inválida')



