from random import randint
cont = 0
print(20 * '=-')
print ('\033[1;33mVAMOS JOGAR PAR OU IMPAR!!\033[m')
print(20 * '=-')
while True:
    print(40 * '-')
    computador = randint(1, 10)
    jogador = int(input('Escolha um número: '))
    escolha = str(input('Par ou Impar: ')).upper().strip()
    print(40 * '-')
    soma = computador + jogador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {jogador} \nE o computador jogou {computador}. \nO total foi de: {soma}, DEU: {resultado}')
    if resultado == escolha:
        print('\033[4;32mVocê Venceu!!\033[m Vamos jogar de novo!!')
        cont += 1
    else:
        break
print('\033[1;31mGAME OVER!! O Computador venceu.\033[m')
print(f'\033[4;34mVocê Venceu {cont} vezes\033[m')
