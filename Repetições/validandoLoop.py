#Validadando valores com loop

x = int(input('Digite um valor maior do que 0: ')) #Recebo um valor fora para fazer o primeiro teste

while(x <= 0): #Primeiro teste
    x = int(input('Digite um valor maior do que 0: ')) #Segundo teste caso o primeiro falhe, o loop continuará até o valor ser maior que 0

print(f'O valor {x} é maior do que 0, encerrando o programa... ')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5

#Exemplo 2

#Saindo quando quiser

print('Digite uma mensagem que irei repetir')
print('Para encerrar, digite "sair"')

mensagem = input('Digite uma mensagem: ')
while(mensagem != 'sair'):
    mensagem = input('Digite uma mensagem: ')
print('Encerrando o programa')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5
