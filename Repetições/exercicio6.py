#Exercício
#Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final.
#Para este intervalo especificado pelo usuário, calcule e mostre na tela:

#A quantidade de números inteiros e positivos;
#A quantidade de números páres;
#A quantidade de números ímpares;
#A respectiva média de cada um dos itens anteriores;

#Será necessário criar uma variável distinta para cada somatório,
#para cada quantidade e para cada média.

inicial = int(input('Digite um valor: '))
final = int(input('Digite outro valor: '))
i = inicial

qtd_positivos = 0
qtd_pares = 0
qtd_impar = 0

soma_positivos = 0
soma_pares = 0
soma_impar = 0


if(inicial < final):
    while(i <= final):

        if(i > 0): #Positivos
            qtd_positivos = qtd_positivos + 1
            soma_positivos = soma_positivos + i

        if(i % 2 == 0): #Par
            qtd_pares = qtd_pares + 1
            soma_pares = soma_pares + i
        
        else:#impar
            qtd_impar = qtd_impar + 1
            soma_impar = soma_impar + i
    
    
        i = i + 1
    
    media_positivo = soma_positivos / qtd_positivos
    media_par = soma_pares / qtd_pares
    media_impar = soma_impar / qtd_impar
    
    print(f'Quantidade de valores positivos {qtd_positivos}')
    print(f'Soma de números positivos pares {soma_pares}')
    print(f'Quantidade de valores impares {qtd_impar}')
    print(f'Soma de números impares{soma_impar}')
    print(f'Media dos valores positivos {media_positivo}')
    print(f'Media dos números pares{media_par}')
    print(f'Media dos números impares{media_impar}')
else:
    print('Você digitou o valor inicial maior do que o final')
    #Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5