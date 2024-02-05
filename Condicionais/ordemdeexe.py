'''
1-Parênteses;
2-Operadores aritméticos de potenciação e radiciação;
3-Operadores aritméticos de multiplicação, divisão e módulo;
4-Operadores aritméticos de soma e subtração;
5-Operadores relacionais; <> = != ==
6-Operador lógico "not";
7-Operador lógico "and";
8-Operador lógico "or";
9-Atribuições.
'''
a = 5
b = 20
result = not a < b
print(result)

c = 15
d = 14
e = 13
result2 = (c < d) or (d > e)
print(result2)

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x
print(res)

'''
Veja a sequencia de passos para a expressão do último exemplo:

        Operação aritmética de divisão: 5.5 / 10 = 0.55;
        Operação aritmética de adição y + 0.55: 1 + 0.55 = 1.55;
        Operações lógicas relacionais. Como temos três delas, ficam:
            x > y → 10 > 1 = True;
            z == y → 5.5 == 1 = False;
            y != 1.55 → 1 != 1.55 = True;
        Operação lógica not False = True;
        Operação lógica and: True and True = True;
        Operação lógica or: True or True = True
'''