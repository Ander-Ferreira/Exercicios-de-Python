def valida_int(pergunta, min, max):
    a = int(input(pergunta))
    while a < min or a > max:
        a = int(input('Valor fora do intervalo. ' + pergunta)) # Solicita novo valor se estiver fora do intervalo
    return a

# Programa principal:
a = valida_int('Digite um valor inteiro entre 0 e 100: ', 0, 100)
print(f'Você digitou {a}. Encerrando o programa')

    #Vejam em: https://colab.research.google.com/drive/1lSj-1gudaYfCKrfcG45ruwssZnvDNyCg?authuser=1#scrollTo=3S91WJfxrxBD
