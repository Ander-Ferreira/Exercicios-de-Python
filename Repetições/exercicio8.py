#Escreva um algoritmo que cálcule a média dos números pares de 1 até 100 (1 incluso e 100 incluso)
#Implementar o laço for

soma = 0
quantidade = 0

for contador in range(1, 101, 1):
    
    if(contador % 2 == 0): #Teste para ver se o valor é par
        soma += contador
        quantidade += 1

media = soma / quantidade


print(f'A média é de {media}')

