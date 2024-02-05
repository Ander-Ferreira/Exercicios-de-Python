#Continue irá repetir o laço até que a condição seja verdadeira

login = input('Digite o seu login: ')

while True:
    
    login = input('Digite o seu login: ')
    
    if(login != 'Anderson'):
        continue #irá continuar o loop até que o login seja Anderson, ou seja, volta para o início do Laço, encerrando o loop o código executará o campo da senha
    
    senha = input('Digite sua senha: ')
    
    if(senha == '12345' ):
        break #irá encerrar o programa, é preciso de um break neste caso quando não há condição no while

print('Acesso concedido')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5