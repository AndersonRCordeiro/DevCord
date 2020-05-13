def jogar():

    print('********************************')
    print('***Bem vindo ao jogo de Forca***')
    print('********************************')

    enforcou = False
    acertou = False
    palavra_secreta = 'banana'

    while(not acertou and not enforcou):
        index = 1
        chute = input('Chute uma letra: ')
        for letra in palavra_secreta:
            if(chute == letra):
                print('Achei a letra: {} na posição: {}'.format(chute
                                                                , index)
                      )
            index = index + 1
        print('jogando...')


if(__name__ =='__main__'):
    jogar()