#Exercicio7
#Escreva um algoritmo em python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas.
#Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
#Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
#O algoritmo deve calcular o preço total a pagar do produto escolhido e mostra-la na tela.
#Considere que uma maçã cuta 2.30, uma laranja 3.60 e uma banana 1.85.

print('Escolha a fruta que deseja comprar')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

opcao = int(input('Digite um número: '))
opcao2 = int(input('Digite a quantidade: '))

if(opcao == 1):
    maca = opcao2 * 2.30
    print(f'Suas {opcao2} maçãs custam ao todo R${maca:.2f}')

else:
    if(opcao == 2):
       laranja = opcao2 * 3.60
       print(f'Suas {opcao2} laranjas custam ao todo R${laranja:.2f}')
    if(opcao == 3):
      banana = opcao2 * 1.85
      print(f'Suas {opcao2} bananas custam ao todo R${banana:.2f}')
    else:
       print('Valor inválido')
#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=jNcUl9dJLNGp