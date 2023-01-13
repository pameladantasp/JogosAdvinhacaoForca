import random
def jogar():
    print('\n################################################')
    print('\t Bem vindo ao jogo da Forca')
    print('################################################')

    with open("palavras.txt") as arquivo:
        palavras = []

        for linha in arquivo:    # acessa as linhas e armazena na lista.
            linha = linha.strip()   # para tirar o \n do final.
            palavras.append(linha)

    numero_aleatorio = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero_aleatorio].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6

    print(len(palavra_secreta))
    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input('\nQual a letra? ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print('Ops, você errou! Faltam {} tentativas.'.format(tentativas - erros))

        if (erros == tentativas):
            print("\nQue pena, você perdeu. A palavra era {}.".format(palavra_secreta.lower()))
            break

        if ("_" not in letras_acertadas):
            print(letras_acertadas)
            print("\nParabéns! Você ganhou!!")
            break
        print(letras_acertadas)


        enforcou = erros == 6
        acertou = '_' not in letras_acertadas


    print('Fim de jogo!')
    print('################################################')

if (__name__ == '__main__'):
        jogar()

