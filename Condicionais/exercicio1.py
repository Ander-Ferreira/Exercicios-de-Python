#Desenvolva um algoritmo que seja capaz de cálcular a soma e a subtração entre dois valores com vírgula
#Crie duas váriaveis de teste. Uma que testa se a soma é maior que 10
#Outra que testa se a subtração é menor do que 0

valor = float(input('Digite um valor: '))
valor2 = float(input('Digite outra valor: '))
soma = valor + valor2
subtracao = valor - valor2
if(valor > 10):
    print(f'{soma} é maior do que 10')
if(valor < 0):
    print(f'{subtracao} é menor do que 0')

#Para o resultado visite: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=RE0xc8FxFbe6