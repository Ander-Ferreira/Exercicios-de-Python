#Crie um programa que calcule a tabuada de um número escolhido pelo usuário
#Imprima na tela a tabuada deste número de 1 a 10. Ao realizar a impressão na tela, mostre os valores formatados conforme a
#seguir
#Exemplo com a tabuada do 5: 1x5=5, 2x5=10, 3x5=15...

tabuada = int(input('Digite um número: '))

print(f'TABUADA DO {tabuada}')

i = 1

while(i <= 10):
  print(f'{tabuada} x {i} = {tabuada * i}')
  i = i + 1