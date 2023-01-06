print("################################################")
print('\t Bem vindo ao jogo de adivinhação')
print("###############################################")

numero_secreto = 20

chute = input('Digite seu numero: ')
# a var chute está armazenando o input que pergunta ao usuário
chute = int(chute)
# convertendo o tipo pois o input é do tipo string

print('Você digitou', chute, '.')

acertou = (chute == numero_secreto)  # parenteses opcional
maior   = (chute > numero_secreto)
menor   = (chute < numero_secreto)

if (acertou):  # O parenteses é opcional. É melhor para deixar claro qual a condição que está sendo usada
    print('Acertou o número secreto! \n')
else:
    if (maior):
        print('Você errou. Seu número foi maior que o número secreto! \n')
    elif(menor):  #if (chute < numero_secreto): -- Não tem necessidade pois essa condição já é contrária do if
        print('Você errou. Seu número foi menor que o número secreto! \n')



print('Fim do jogo!')
print("###############################################")