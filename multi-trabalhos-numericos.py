from time import sleep
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
opcoes = 0
while opcoes != 5:
    opcoes = int(input( '''
    [1] Somar
    [2] Multiplicar
    [3] Maior 
    [4] Novos Números
    [5] Sair do programa
    Qual sua opção? '''))
    print(10 * '=-')
    if opcoes == 1:
        print('{} + {} é: {}'.format(n1, n2, (n1+n2)))

    elif opcoes == 2:
        print('{} x {} é: {}'.format(n1, n2, (n1 * n2)))

    elif opcoes == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior é: {}'.format(n1, n2, n2))

    elif opcoes == 4:
        print('Informe os numeros novamente!!')
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
    elif opcoes == 5:
        print('FINALIZANDO...')

    else:
        print('OPÇÃO INVÁLIDA!! Tente novamente:')
    print(10 * '=-')
    sleep(1.5)
print('FIM DE PROGRAMA!!')
print('VOLTE SEMPRE!!')