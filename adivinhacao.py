import random

numero_secreto = random.randrange(1, 101)
total_tentativas = 3

print("################################################")
print('\t Bem vindo ao jogo de adivinhação')
print("################################################")

cont = 0

while True:  # improvisando um 'do-while' para aceitar somente as alternativas passadas
    print('Qual o nível de dificuldade desejado?')
    nivel = int(input('(1) Fácil  |  (2) Médio  |  (3) Difícil : '))
    cont += 1
    if nivel == 1:
        total_tentativas = 20
        break
    elif nivel == 2:
        total_tentativas = 10
        break
    elif nivel == 3:
        total_tentativas = 5
        break

for rodada in range(1, total_tentativas + 1):
    print("\n>>> Tentativa {} de {} <<<".format(rodada, total_tentativas))

    chute = input('Digite um número de 1 a 100: ')
         # a var chute está armazenando o input que pergunta ao usuário
    chute = int(chute)
         # convertendo o tipo pois o input é do tipo string, poderia ter feito direto, como na linha 11 visto depois

    print('\nVocê digitou', chute)

    if (chute < 1 or chute > 100):
        print('Valores menores que 1 e maiores que 100 não são permitidos. \n')
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print('Parabéns!! Você acertou o número secreto! \n')
        break
    else:
        if maior:
            print('Você errou. Seu número foi maior que o número secreto! \n')
        elif menor:     #if (chute < numero_secreto): -- Não tem necessidade pois essa condição já é contrária do if
            print('Você errou. Seu número foi menor que o número secreto! \n')

    rodada += 1

if acertou == False:
    print('O número secreto era {}.'.format(numero_secreto))

print('\tFim do jogo!')
print("################################################")

