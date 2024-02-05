#Interrompendo loop com Break

while True: #Não há uma condição, sempre estará rodando
    
    mensagem = input('Digite uma mensagem a ser repetida: ')
    print(f'{mensagem}')
    
    if(mensagem == 'sair'):#condição para encerrar o programa
        break

print('Encerrando o programa')

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5