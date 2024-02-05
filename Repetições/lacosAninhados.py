#While dentro de While

tabuada = 1

while (tabuada <= 10):
    print(f'Tabuada {tabuada}')
    i = 1
    
    while (i <= 10):
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    
    tabuada += 1

#2x Laços for

for tabuada in range(0, 11, 1):
    print(f'Tabuada {tabuada}')
    for i in range(0, 11, 1):
        print(f'Tabuada de {tabuada} x {i} = {tabuada * i}')


#While e For

tabuada = 0

while(tabuada <= 10):
    print(f'Tabuada {tabuada}')
    
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')
    
    tabuada += 1

