#Desenvolva um algoritmo que seja capaz de calcular a soma e a subtração entre 2 valores com vírgula.
#Crie duas variáveis de teste. Uma que testa se a soma é maior que 10.
#Outra que testa se a subtração é menor do que 0. Imprima tudo na tela.

valor1 = float(input('Digite um valor com virgula: '))
valor2 = float(input('Digite outro valor com vírgula: '))
soma = valor1 + valor2
subtracao = valor1 - valor2
condSoma = soma > 10
condSub = subtracao < 0
print(f'A o resultado da soma foi de {soma:.2f} sendo um valor > 10 {condSoma}, e o resultado da subtração {subtracao:.2f} sendo um valor 0 < {condSub}')
#:.2f é usado para restringir o número de casas decimais depois da vírgula do valor float
#Veja o resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=DIVKFoAD2ZKU