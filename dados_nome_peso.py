registro = list()
dados = list()
while True:
    registro.append(str(input("Digite um nome: ")))
    registro.append(float(input("Digite um peso em KG: ")))
    if len(dados) == 0:
        maior = menor = registro[1]
    else:
        if registro[1] > maior:
            maior = registro[1]
        if registro[1] < menor:
            menor = registro[1]
    dados.append(registro[:])
    registro.clear()
    fim = input("Deseja continuar? S/N: ").upper()
    if 'N' in fim:
        break
print("="*30)
print(f'Foram cadastradas {len(dados)} pessoas')
print(f'O maior peso foi {maior}KG. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')
        


    
