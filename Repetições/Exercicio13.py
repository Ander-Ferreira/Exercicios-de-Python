#Exercicio
#Escreva um algoritmo que leia números inteiros via teclado.
#Somente valores positivos devem ser aceitos pelo programa.
#Ao final da execução, informe a média dos valores digitados.

#Realize implementação com as instruções break e continue, e trabalhe com operações lógicas truthy e falsey.

#Não se esqueça de empregar também operadores especiais de atribuições


while(num < 0 or num != int):
    
    falsey = 0
    
    num = int(input('Digite um número inteiro positivo: '))
    num2 = int(input('Digite outro valor inteiro positivo: '))

    if(num > -1):
        truthy = 1
        num += num2
        break

print(f'A média dos valores digitados é {num / 2} ')


#Outra forma de resolver


soma = 0
i = 0 #Contador

while True: #Enquanto for maior do que 0 execute o laço abaixo.
    num = int(input('Digite um valor: '))
    
    if(num <= 0):
        break

    soma += num

    i += 1

mediia = soma / i #Saindo do laço, faça a média dos valores digitados no laço

print(f'A média dos valores é {mediia}')



#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5