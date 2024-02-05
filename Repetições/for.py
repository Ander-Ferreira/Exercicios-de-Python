#Laço for(para)

#Laço for é utilizado quando temos uma certeza da quantidade de repetições que a gente quer fazer:



for i in range(6): #O valor padrão de i = 0, e o intervalo vai de 0 até 5, excluindo o 6, sempre é -1 casa que irá mostrar
    print(i)



#Faça um programa em Python para exibir na tela uma contagem regressiva do lançamento de um foguete
#Iniciando em 10 até 0, escrevendo após o 0 a palavra Fogo!


for contador in range(10, -1, -1): #Contador irá contar de 10 até -1 de menos um em menos 1, range é a função de intervalo
    print(contador)

print('Fogo!')
