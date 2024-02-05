def funcao(x = 0, y = 0, z = 0): #Passamos o valor padrão para as variáveis x, y, z para que o usuário não precise digitar, ou como valor padrão antes do usuário digitar
    soma = x + y + z
    print(soma)

#Imprimindo a função com três exemplos
funcao(1,2,3)
funcao(1,2)
funcao(1)
funcao()


def funcao2(a = 0, b = 0, c = 0, d = False):
    soma2 = a + b + c
    if d:
        print(soma2)

funcao2(1,2,3, True) #Mudamos o valor para True para que a impressão aconteça
    