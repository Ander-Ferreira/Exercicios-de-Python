#Escreva um algoritmo que lê um valor inteiro qualquer.
#Após verifique se este valor está contido dentro dos seguintes intervalos: -100 < x < -1 ou 1 < x < 100.
#Imprima na tela uma mensagem caso ele esteja em um dos intervalos.



#Passo a passo

num = int(input('Digite um número: '))
if(((num > -100) and (num < -1)) or ((num > 1) and (num < 100))):
    print('Está no intervalo')
else:
    print('Não está no intervalo')

#Segunda maneira

num1 = int(input('Digite um número: '))
if(num1 >= -100 and num1 <= 100):
    print('Está no intervalo')
else:
    print('Está fora do intervalo')


#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=jNcUl9dJLNGp
