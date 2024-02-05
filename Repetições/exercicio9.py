#Crie um programa que calcule a tabuada de um número escolhido pelo usuário
#Imprima na tela a tabuada deste número de 1 a 10. Ao realizar a impressão na tela, mostre os valores formatados conforme a
#seguir
#Exemplo com a tabuada do 5: 1x5=5, 2x5=10, 3x5=15...
#Usando laço for

print('Tábuada de vezes')
num = int(input('Digite um número que deseja a tábuada: '))

for contador in range(0, 11, 1):
    resultado = num * contador
    print(f'O resultado de {num} x {contador} = {resultado}')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5






