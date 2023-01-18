import random

def jogar():
    
    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    # Mostra as letras acertadas
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
            valida_chute_correto(palavra_secreta, chute, letras_acertadas)

        else:
            erros += 1
            desenha_forca(erros, tentativas)
        
        print(letras_acertadas)
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas   # Se acabou os campos _ significa que o usuário acertou todas letras

        if (erros == tentativas):
            mensagem_perdedor(palavra_secreta)
            break

        if (acertou):
            mensagem_vencedor()
            break

    print('Fim de jogo!')
    print('################################################')


def valida_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1    


def mensagem_abertura():
    print('\n################################################')
    print('\t Bem vindo ao jogo da Forca')
    print('################################################')


def carrega_palavra_secreta(nome_arquivo='palavras.txt'):   # alternativa diferente para puxar o arquivo, a anterior era:
   with open(nome_arquivo, 'r' ) as arquivo:                #  carrega_palavra_secreta(): with open ('palavras.txt', 'r') as arquivo..
        palavras = []

        for linha in arquivo:    # acessa as linhas e armazena na lista.
            linha = linha.strip()   # para tirar o \n do final.
            palavras.append(linha)

        numero_aleatorio = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero_aleatorio].upper()
        return palavra_secreta



def desenha_forca(erros, tentativas):
    print('Ops, você errou! Faltam {} tentativas.'.format(tentativas - erros))

    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_perdedor(palavra_secreta):
    print("\nQue pena, você foi enforcado! A palavra era {}.".format(palavra_secreta.lower()))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mensagem_vencedor():
    print("\nParabéns! Você ganhou!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if (__name__ == '__main__'):
        jogar()