matriz = [[0,0,0],[0,0,0],[0,0,0]]
num = 0
soma_par = 0
soma_coluna3 = 0
for l in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite o número da posição [{l}][{c}]: '))
        matriz[l][c] = num
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        soma_coluna3 += matriz[l][2]

maiorvalor_linha2 = max(matriz[1])
print("="*30)
print(f'A soma dos números pares é {soma_par}')
print(f'A soma dos números da 3° coluna é {soma_coluna3}')
print(f'O maior valor da 2° linha é {maiorvalor_linha2}')
