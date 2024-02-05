#Escreva um algoritmo que encontre todos os números primos de 2 até 99. Imprima na tela todos eles.

print('Primos de 2 até 99')

for numero in range(2, 100, 1):
    
    testeBolean = 0 #Testa se o valor continua sendo primo

    for i in range(2, numero, 1):
        
        if(numero % i ==0): #Teste, se for divisível por 0, o número já não é primo, o laço voltará para e testará o restante.
            testeBolean = 1
            break
    
    if(testeBolean == 0): #Se o valor continua sendo primo, imprima ele
        print(numero)

    

