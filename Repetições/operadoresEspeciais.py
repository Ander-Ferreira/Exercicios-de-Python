#Operadores especiais de atribuição

#Soma  += x que é equivalente a Soma = soma + x

#Subtraçãos -= x que é equivalente a Subtração = Subtração - x

#Multiplicação *= x que é equivalente a Multiplicação = Multiplicação * x

#Divisão /=  x que é equivalente a Divisão = Divisão / x

#Potencialização **= x que é equivalente a Potencialização = Potencialização ** x

#DivisãoInteira //= x que é equivalente a DivisãoInteira = DivisãoInteira // x

#Exemplo de uso com laço While

x = 1
while(x <=5):
    print(x)
    x +=1 #Equivale a x = x + 1

#Exemplo 2

soma = 0
cont = 0

while(cont <= 5):
    x = int(input(f'Digite um número: {cont} '))
    soma += x
    cont += 1

print(f'Somatório de {soma}')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5

