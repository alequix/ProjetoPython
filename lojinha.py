total = prodmil = cont = menor = 0
resposta = ' '
barato = ''
print(25 * '-_')
print('               LOJA DO LECÃO           ')
print(25 * '-_')
while True:
    produto = str(input('Qual o produto comprado? ')).strip()
    valor = float(input('Qual o preço? R$'))
    total += valor
    cont += 1
    print(40 * '-')
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
    print(40 * '-')
    if valor > 1000:
        prodmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O valor total das compras foi de R${total:.2f}')
print(f'Tivemos um total de {prodmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi: {barato}, custando o valor de: {menor:.2f}')