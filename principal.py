import forca
import advinhacao
print('Escolha um jogo: ')
jogo = int(input('(1) - Advinhação, (2) - Forca '))

if(jogo == 1):
    print('Jogando Advinhacao')
    advinhacao.jogar()
elif(jogo == 2):
    print('Jogando Forca')
    forca.jogar()
else:
    print('opção invalida')