print("################################################")
print('\t Bem vindo ao jogo de adivinhação')
print("###############################################")

numero_secreto = 20

total_tentativas = 3
rodada = 1

while rodada <= total_tentativas:
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute = input('Digite seu numero: ')
         # a var chute está armazenando o input que pergunta ao usuário
    chute = int(chute)
         # convertendo o tipo pois o input é do tipo string

    print('Você digitou', chute)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        rodada = total_tentativas + 2
        print('\nParabéns!! Você acertou o número secreto! \n')
    else:
        if (maior):
            print('\nVocê errou. Seu número foi maior que o número secreto! \n')
        elif(menor):     #if (chute < numero_secreto): -- Não tem necessidade pois essa condição já é contrária do if
            print('\nVocê errou. Seu número foi menor que o número secreto! \n')

    rodada += 1

print('\tFim do jogo!')
print("###############################################")
