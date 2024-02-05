#Truthy e Falsey são boleanos falsificados
#Truthy é tudo que contém algo, sendo de 1 até "string"
#Falsey é tudo que não contém algo, seja de 0 até vazio sem espaço ''

numero = 1 #mude para 0 para ser falsey

if numero:
    print('É Truthy')

else:
    print('É Falsey')



palavra = "" #coloque algo dentro para ser Truthy

if palavra:
    print('É Truthy')
else:
    print('É Falsey')



nome = ''

while not nome:
    nome = input('Digite seu nome')
    valor = int(input('Digite um número qualquer: '))

    if valor:
        print('Você digitou um número diferente de zero')
    else:
        print('Você digitou zero')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5
