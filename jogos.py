import adivinhacao
import forca

def escolhe_jogo():
    print('################################################')
    print('\t ESCOLHA UM JOGO DISPONÍVEL ')
    print('################################################')

    cont = 0
    while True:
        jogo = int(input('(1) Adivinhção  |  (2) Forca  : '))

        cont += 1
        if jogo == 1:
            adivinhacao.jogar()
            print('\n')
            break
        elif jogo == 2:
            forca.jogar()
            print('\n')
            break

if (__name__ == '__main__'):
    escolhe_jogo()
