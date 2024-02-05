
#O returno é como o print, só que da função, ele retorna um valor da função.

def parImpa(x):
    if(x % 2 == 0):
        return "É par"
    else:
        return "É impar"


valor = int(input('Digite um valor: '))

print(parImpa(valor))


#Vejam em: https://colab.research.google.com/drive/1lSj-1gudaYfCKrfcG45ruwssZnvDNyCg?authuser=1#scrollTo=3S91WJfxrxBD