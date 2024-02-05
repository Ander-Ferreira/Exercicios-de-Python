#Suponhamos que desejamos exibir uma série de números na tela,
#Onde os limites de início e fim dessa sequência são determinados pelo usuário que exectua o programa.
#Crie um algoritmo que leia os valores de início e de fim de novo programa,
#e imprima na tela o intervalor de números pares correspondentes.


inicial = int(input('Digite um número: '))
final = int(input('Digite outro número: '))
i = inicial

while(i <= final):
    if(i % 2 == 0):
        print(i)
    i = i + 1

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5