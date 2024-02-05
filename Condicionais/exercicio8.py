#Exercicio 8
#Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, Laranjas ou Bananas.
#Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para Laranja e 3 para banana.
#Após escolhidas as frutas, deve-se digitar quantas unidades se quer comprar.
#O algoritmo deve calcular o preço total a pagar do produto escolhido e mostra-la na tela.
#Considere que uma maçã custa 2.30, uma laranja 3.60 e uma banana 1.85
#Ultilize a estrutura elif

print('Escolha as frutas que quer')
print('1 - para Maçã')
print('2 - para Laranja')
print('3 - para Banana')

menu = int(input('Digite um valor: '))
quantidade = int(input('Digite a quantidade: '))

if(menu == 1):
    maca = 2.30 * quantidade
    print(f'Sua(as) {quantidade} de Maçãs ao todo é R${maca}')

elif(menu == 2):
    laranja = 3.60 * quantidade
    print(f'Sua(as) {quantidade} Laranja(as) ao todo é R${laranja}')
elif(menu == 3):
    banana = 1.85 * quantidade
    print(f'Sua(as) {quantidade} Banana(as) ao todo é {banana}')

#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=jNcUl9dJLNGp