#Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias,
#De horas, de minutos e segundos
#Calcule o total de segundos resultante e imprima na tela para o usuário

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos'))
segundosTotal = segundos + (dias * 24 * 60 *60) + (horas * 60 * 60) + minutos * 60
print(f'O total de segundos ao todo foi de {segundosTotal}')

#Para o resultado visite https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=c8dsUhNyzh6L