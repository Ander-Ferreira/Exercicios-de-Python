nome = input('Qual é o seu nome?') #Gera uma variável de entrada, onde será inserido um valor pelo usuário que será atribuído a variável nome
print(nome)

idade = input('Digite sua idade: ')
print(f'Olá{nome}, sua idade é {idade}')


#Problema que pode acontecer
'''
Se eu não converter o valor para número, ele irá concatenar os números ao invés de fazer uma operação,
para isso usamos o float() com os valores dentro, exemplo abaixo:
'''

num1 = float(input('Digite um número: ')) #serve como int() para inteiro também
num2 = float(input('Digite ou número: '))
print(num1 + num2)

#Visite a o link para ver os códigos rodando: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=sUU6K3PPeysn
