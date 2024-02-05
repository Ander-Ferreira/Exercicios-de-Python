#Crie um programa que calcule a soma de 5 valores inteiros. 
#Cada valor a ser somado é digitado pelo usuário.
#Imprima a soma na tela.
#Após a soma, calcule também a média dos valores e mostre na tela.

soma = 0
i = 1
while(i <= 5):
    x = int(input(f'Digite um número{i}: '))
    soma  = soma + x
    i = i + 1

media = soma / 5

print(f'A soma é de {soma}, e a média é de {media}')