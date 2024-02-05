#Faça um programa em Python para exibir na tela uma contagem regressiva do lançamento de um foguete
#Iniciando em 10 até 0, escrevendo após o 0 a palavra Fogo!

cont = 10

while True:
    if(cont != 0):
        print(cont)
        cont -= 1
    if(cont == 0):
        break

print(f'{cont} Fogo!')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5
