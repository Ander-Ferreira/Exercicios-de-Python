#Escreva uma rotina que crie um laço de repetição que faz uma contagem
#E imprime esta contagem na tela em uma só linha.
#Porém, como parâmetro, a função deve receber o valor inicial da contagem, o final, e o passo da iteração.
#Deixe os parâmetros incial e de passo como opcionais.
#Você pode fazer o laço com for ou while.

#def contar(inicio = 0, fim, passo = 1): dá erro se houver um valor no meio sem igualdade, então organize assim:

def contar(fim, inicio = 0, passo = 1):
        for tamanho in range(inicio, fim, passo):
            print(f'{tamanho}', end='') #end='' junta os números em uma linha só

contar(6, 1, 1) #Primeiro o fim, depois o inicio, e depois o passo+