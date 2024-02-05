#Escreva uma rotina que recebe três valores como parâmetro e coloque-os em ordem crescente,
#Ou seja, o menor ao maior.
#Imprima na tela os três valores.


def maiorMenor(valor1, valor2, valor3):
    
    if ((valor1 > valor3) and (valor1 > valor2)):
        if(valor2 > valor3):
            print(f'Ordem crescente: {valor3}, {valor2}, {valor1}')
        else:
            print(f'{valor2}, {valor3}, {valor1}')
        
    elif((valor2 > valor1) and (valor2 > valor3)):
        if(valor1 > valor3):
            print(f'Ordem crescente: {valor3}, {valor1}, {valor2}')
        else:
            print(f'{valor1}, {valor3}, {valor2}')
        
    elif((valor3 > valor1) and (valor3 > valor2)):
        if(valor1 > valor2):
            print(f'Ordem crescente: {valor2}, {valor1}, {valor3}')
        else:
            print(f'{valor1}, {valor2}, {valor3}')

x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
z = int(input('Digite outro valor: '))

maiorMenor(x, y, z) #A função recebe como parâmetro os números digitados

#Vejam em: https://colab.research.google.com/drive/1lSj-1gudaYfCKrfcG45ruwssZnvDNyCg?authuser=1#scrollTo=3S91WJfxrxBD