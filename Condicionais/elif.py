#Lê dois valores inteiros


x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if(x > y):
    print('O primeiro valor é maior que o segundo')
elif(x < y): #É o mesmo que o if dentro do else das condições aninhadas
    print('O segundo valor é maior que o primeiro!')
else:
    print('Ambos valores são iguais!')

#Outro exemplo
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if(nome == 'Vinicius'):
    print('Olá, Vinicius')
elif(idade < 18):
    print('Você não é o Vinicius, e é menos de idade.')
elif(idade > 100):
    print('Você não é o Vinicius, e é imortal!')

#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=jNcUl9dJLNGp
