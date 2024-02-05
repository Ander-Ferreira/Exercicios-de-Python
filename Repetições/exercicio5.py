#Escreva um algoritmo que leia dois valores e imprima na tela o resultado da multiplicação de ambos.
#Porém, para calcular a multiplicação, utilize somente operações de soma e subtração.
#Lembrando que uma multiplicação pode ser considerada como um somatório sucessivo.
#Utilize esta lógica para construir seu algoritmo.

num1 = int(input('Digite um valor: '))
vezes = int(input('Digite outro valor: '))
i = 1
multi = 0
while(i <= vezes ):
    multi = multi + num1
    i = i + 1
print(multi)
