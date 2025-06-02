filme = 'Ratatouille'
lista: list= []
def checar():
    for letra in filme:
        for letra_lista in lista:
            
            if letra.lower() == letra_lista.lower(): 
                print(letra)
            
    

while True :
    letra_nova = input('digite uma letra: ')
    if letra_nova in lista:
        print('essa letra ja existe')
    else: 
        lista.append(letra_nova)
    #COMO O CODIGO FUNCIONA
    # vai_inserir = True
    # for letra_lista in list:
    #     if letra_nova == letra_lista:
    #         print('essa litra ja existe')
    #         vai_inserir = False
    # if vai_inserir:
    #     list.append(letra_nova)
    # print(list)
    checar()

    


