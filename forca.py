
def jogar():
    print('################################################')
    print('\t Bem vindo ao jogo da Forca')
    print('################################################')

    palavra = 'pamela'
    enforcou = False
    acertou = False
    tentativas = 7

    while (not enforcou and not acertou):   # enforcou == False and acertou == False
        print('playing...')

        chute = input('Qual a letra? \n')
        chute.strip()  # strip apaga o espaço em branco no início/fim da entrada de dado

        index = 1

        # para cada letra do usuário, comparamos com o chute dele, se o chute for igual, exibiremos.
        for letra in palavra:
            if (chute.upper == letra.upper):  # para não ter distinção de minuscula e maiuscula
                print('Letra "{}" encontrada na posição {}'.format(letra, index))
                tentativas -= 1
                index += 1
            else:
                print('Letra não encontrada')


    print('Fim de jogo!')
    print('################################################')

if (__name__ == '__main__'):
        jogar()


