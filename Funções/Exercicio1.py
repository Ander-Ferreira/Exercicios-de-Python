#Escreva uma rotina que crie uma borda ao redor de uma palavra para destaca-la como sendo um título.
#A rotina deve receber como parâmetro a palavra a ser destacada.
#O tamanho da caixa de texto deverá ser adaptável de acordo com o tamanho da palavra.
#A seguir veja alguns exemplos de como deve ficar a borda na palavra.

# +---------+
# |Anderson |
# +---------+ 

def borda(s1):
    tamanho = len(s1) #Pega o tamanho da string que será passada como parâmetro lá embaixo
    
    if tamanho: #Só coloca o tracejado se houver uma string.
        print('+','-' * tamanho,'+') #vai colocar traço de acordo com o tamanho da string s1 que será passada lá embaixo
        print('|', s1, '|')
        print('+','-' * tamanho,'+')

#Execução
borda('Aaaaaa')