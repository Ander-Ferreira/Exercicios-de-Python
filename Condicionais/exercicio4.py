#Exercício 3
#Um aluno, para passar de ano, precisa estar aprovado em todas as matérias que ele está cursando.
#Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
#Escreva um algoritmo que leia a nota final do aluno em cada matéria, e informe na tela se ele passou de ano ou não.

matematica = float(input('Digite sua nota: '))
portugues = float(input('Digite sua nota: '))
ciencias = float(input('Digite sua nota: '))
media = 7
if((matematica and portugues >= 7) and ciencias >= 7 ):
            print('Aprovado')
else:
        print('Reprovado')

#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=jNcUl9dJLNGp
