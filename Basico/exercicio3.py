#Desenvolva um algoritmo que solicite ao usuário o preço de um produto
#Um percentual de desconto a ser aplicado a ele
#Calcule e exiba o valor do desconto e o preço final

preco = float(input('Digite o preço: '))
desconto = int(input('Digite o desconto de 0-100%: '))
precoDesconto = preco * (desconto / 100)
precoFinal = preco - precoDesconto
print(f'O desconto foi de R${precoDesconto}, ficando o preço final de R${precoFinal}')

#Veja o resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=DIVKFoAD2ZKU
