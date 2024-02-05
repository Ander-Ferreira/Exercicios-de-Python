#Uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de 5 anos de empresa.
#Ainda, funcionários com mais de 10 anos de empresa tem direito a uma bonificação de 30%.
#Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente.
#Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa,
#e apresente a bonificação de cada funcionário na tela.

salario = float(input('Digite seu salário: '))
tempo = float(input('Digite seu tempo de empresa: '))

if((tempo > 5) and (tempo < 11)):
    maisde5 = (salario * 0.2) + salario
    print(f'Seu salário aumentou 20%, agora está {maisde5}')
else:
    if(tempo > 10):
        maisde10 = (salario * 0.3) + salario
        print(f'Seu salário aumentou 30%, agora é {maisde10}')
    else:
        menosde5 = (salario * 0.05) + salario
        print(f'Seu salário aumentou 5%, agora é {menosde5}')

#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=jNcUl9dJLNGp
    
