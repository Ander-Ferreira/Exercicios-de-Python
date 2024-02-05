#Uma empresa concedeu um bônus de 20% para todos seus fincionários com mais de 5 anos de empresa.
#Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente.
#Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa,
#e apresente a bonificação de cada funcionário na tela.

anosEmpresa = int(input('Digite seus anos na empresa: '))
salario = float(input('Digite seu salário: '))

if(anosEmpresa > 5):
    anoDentro = ((20 / 100) * salario) + salario
    print(f'Seu salário ganhou 20% de aumento, agora é {anoDentro}')
else:
    anoFora = ((10 / 100) * salario) + salario
    print(f'Você ganhou 10% de aumento, seu salário agora é {anoFora}')
        
#Para o resultado visite: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=RE0xc8FxFbe6