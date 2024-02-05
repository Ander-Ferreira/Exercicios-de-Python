#Exercicio
#Escreva um algoritmo que repetidamente pergunte ao usuário qual sua idade e seu sexo (M ou F)
#Para cada resposta o programa deve imprimir a mensagem:

#"Boa noite, Senhor. Sua idade é [IDADE]". Caso o gênero for masculino
#"Boa noite, Senhora. Sua idade é [IDADE]". Caso gênero for feminino.

#O programa deve encerrar quando o usuário digitar uma idade negativa.

print('Digite sua idade e gênero')

idade = int(input('Digite sua idade: '))
genero = input('Digite seu gênero, M ou F: ')


while(idade > 0):
    if(genero == 'M'):
        print(f'Boa noite, Senhor. Sua idade é {idade}')
        genero = input('Digite seu gênero, M ou F: ')
        idade = int(input('Digite sua idade: '))
    
    elif(genero == 'F'):
        print(f'Boa noite, Senhora. Sua idade é de {idade}')
        idade = int(input('Digite sua idade: '))
        genero = input('Digite seu gênero, M ou F: ')
    else:
        break

print('Encerrando o programa')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5