#Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela.
#Para fins de simplificação, despreze o dia e o mês do ano.
#Após o cálculo, verifique se a idade é maior ou igual a 18 anos e apresente uma mensagem na tela.
#Informando que já é possível tirar a carteira de motorista caso seja maior

nascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = int(2023)
idade = anoAtual - nascimento
if(idade >= 18):
    print(f'Você tem {idade} anos, é possível tirar a carteira')
if(idade < 18):
    print(f'Sua idade é {idade} anos, não pode tirar carteira')

#Para o resultado visite: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=RE0xc8FxFbe6