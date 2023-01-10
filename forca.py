
def jogar():
    print('################################################')
    print('\t Bem vindo ao jogo da Forca')
    print('################################################')

    palavra = ['b', 'a', 'n', 'a', 'n', 'a']
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    letras_faltando = str(letras_acertadas.count('_'))

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:
        print('playing...')

        chute = input('Qual a letra? \n')
        chute = chute.strip()

        index = 0
        for letra in palavra:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra

            index += 1

        print(letras_acertadas)
        print('Ainda faltam acertar {} letras'.format(letras_faltando))


    print('Fim de jogo!')
    print('################################################')

if (__name__ == '__main__'):
        jogar()


