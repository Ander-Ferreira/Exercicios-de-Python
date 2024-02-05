#Exercício
#Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final.
#Para este intervalo especificado pelo usuário, calcule e mostre na tela:

#A quantidade de números inteiros e positivos;
#A quantidade de números páres;
#A quantidade de números ímpares;
#A respectiva média de cada um dos itens anteriores;

#Será necessário criar uma variável distinta para cada somatório,
#para cada quantidade e para cada média.

valorInicial = int(input('Digite um valor Inicial: '))
valorFinal = int(input('Digite um valor final: '))
quantidadePositivos = 0
quantidadePares = 0
quantidadeImpares = 0
somaPositivos = 0
somaPares = 0
somaImpares = 0
i = 0

if(i <= valorFinal):
    while(i <= valorFinal):
        quantidadePositivos = quantidadePositivos + 1
        somaPositivos = somaPositivos + i
    
        if(i % 2 == 0):
            quantidadePares = quantidadePares + 1
            somaPares = somaPares + i
        else: 
            quantidadeImpares = quantidadeImpares + 1
            somaImpares = somaImpares + i
    
        i = i + 1

media_positivo = somaPositivos / quantidadePositivos
media_par = somaPares / quantidadePares
media_impar = somaImpares / quantidadeImpares

print(f'A quantidade de positivos é de inteiros positivos é de {quantidadePositivos}')
print(f'A quantidade de soma dos positivos é de {somaPositivos}')
print(f'A quantidade de pares é de {quantidadePares}')
print(f'A quantidade da soma de pares é de {somaPares}')
print(f'A quantidade de números impares é de {quantidadeImpares}')
print(f'A quantidade da soma de impares é de {somaImpares}')
print(f'A média de positivos é de {media_positivo}')
print(f'A média par é de {media_par}')
print(f'A média impar é de {media_impar}')
#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5

