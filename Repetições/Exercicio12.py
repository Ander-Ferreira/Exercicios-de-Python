#Escreva um algoritmo que obtenha do usuário uma frase de tamanho entre 10 e 30 caracteres
#Faça a validação deste dado.

#Após a frase ter sido digitada corretamente,
#Faça a impressão dela na tela da maneira exata como foi digitado e, em seguinda,
#Remova os espaços da frase e imprima novamente, sem espaços.

frase = input('Digite uma frase: ')
tamanho = len(frase)

while((tamanho < 10 ) or (tamanho > 30)): #Enquanto a frase for menor do que 10 caracteres ou maior, o laço continuará pedindo a frase
    frase = input('Digite uma frase: ')
    tamanho = len(frase)

print(f'Com espaços: {frase}')
print(f'Sem espaços:', end='')

for i in range(0, tamanho, 1): #caso esteja do tamanho correto a frase
    if(frase[i] != ' '): #Testamos para ver se tem espaço na frase, se tiver passamos para o código abaixo
        print(frase[i], end='') #end='' junta os caracteres do [i].

#Veja também em: https://colab.research.google.com/drive/1GM1al_vIm-AjV6n4QH8kD-aFpkD5-n7t?authuser=1#scrollTo=_COMn47FN3c5