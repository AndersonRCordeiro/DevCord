import random
def jogar():
    print('*******************************')
    print('Bem vindo ao jogo de advinhação')
    print('*******************************')
    print(__name__)

    numero_secreto2 = int(round(random.random()*100))
    numero_secreto = random.randrange(1,101)
    print(numero_secreto)
    print('Entre com o nível de dificuldade')
    nivel = int(input('(1) - Fácil, (2) - Médio, (3) - Difícil '))
    if(nivel == 1):
        numero_de_tentativas = 100
    elif(nivel == 2):
        numero_de_tentativas = 20
    elif(nivel == 3):
        numero_de_tentativas = 5
    else:
        print('Valor Incorreto')
    print('Numero de tentativas: ',numero_de_tentativas)


    chute = 0


    rodada = 1
    pontos = 1000
    #numero_de_tentativas = 3

    for rodada in range(1,numero_de_tentativas+1):
        print('Tentativa {} de {}'.format(rodada, numero_de_tentativas))
        chute_str = input("Digite um valor: ")
        chute = int(chute_str)

        if(chute < 0 or chute >= 100):
            print('Digite um valor entre 0 e 100')
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        pontos_perdidos = 0

        if (acertou):
            print('Acertou! \n')
            break
        else:
            if(maior):
                print('Você erro, seu chute foi maior')
                if (rodada == numero_de_tentativas):
                    print('o número secreto era {}. você fez {} pontos'.format(numero_secreto
                                                                               ,pontos)
                          )
            elif(menor):
                print('Você erro, seu chute foi menor')
                if (rodada == numero_de_tentativas):
                    print('o número secreto era {}. você fez {} pontos'.format(numero_secreto
                                                                               , pontos)
                          )
            pontos_perdidos = abs(numero_secreto - chute)
            print(pontos_perdidos)
            pontos = pontos - pontos_perdidos
            print(pontos)
        #rodada = rodada +1
    print('Fim de Jogo sua pontuação foi: ',pontos)

if(__name__=='__main__'):
    jogar()