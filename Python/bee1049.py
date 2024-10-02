etapa1 = str(input())
etapa2 = str(input())
etapa3 = str(input())

if etapa1 == 'vertebrado':
    if etapa2 == 'ave':
        if etapa3 == 'carnivoro':
            print('aguia')
        elif etapa3 == 'onivoro':
            print('pomba')
    elif etapa2 == 'mamifero':
        if etapa3 == 'onivoro':
            print('homem')
        elif etapa3 == 'herbivoro':
            print('vaca')
elif etapa1 == 'invertebrado':
    if etapa2 == 'inseto':
        if etapa3 == 'hematofago':
            print('pulga')
        elif etapa3 == 'herbivoro':
            print('lagarta')
    elif etapa2 == 'anelidio':
        if etapa3 == 'hematofago':
            print('sanguessuga')
        elif etapa3 == 'onivoro':
            print('minhoca')