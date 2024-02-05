#Uma loja de departamentos está oferecendo diferentes formas de pagamento,
#conforme opções listadas a seguir.
#Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final
#de acordo com a opção escolhida.
#Pagamento à vista - conceder escondo de 5%
#Pagamento em 3x - o valor não sofre alteração
#pagamento em 5x - acréscimo de 2%
#pagamento em 10x - acréscimo em 8%


print('Escolha as opções de Parcelamento')
print('1 - À vista recebe 5% de desconto')
print('2 - 3x sem Juros')
print('3 - 5x com juros de 5%')
print('4 - 10x com juros de 8%')

val = float(input('Digite o valor: '))
opcao = input('Digite uma opção: ')
if(opcao == '1'):
    opcao1 = val - 100 * 0.05
    print(f'O valor de sua compra recebeu 5% de desconto, ficando: R${opcao1}')

elif(opcao == '2'):
    val_final = val / 2
    print(f'O preço do seu produto é: R${val}, com 2 parcelas de {val_final}')

elif(opcao == '3'):
    val_final = val / 3
    opcao3 = 100 * 0.05 + val
    print(f'O preço do seu produto com 5% de juros é: {opcao3}, com três parcelas de {val_final:.2f}')

elif(opcao == '4'):
    val_final = val / 4
    opcao4 = 100 * 0.08 + val
    print(f'O preço do seu produto com 10% de juros é: {opcao4}, com 10 parcelas de {val_final} ')

else:
    print('Opção inválida')



#Resultado em: https://colab.research.google.com/drive/1Rev78gB_PvxipHkhdiZg2AlemdTRjhb8?authuser=1#scrollTo=PJOIAe3UZnYl

