lista = [[],[]]
num = 0

for i in range (0,7):
    valor = int(input(f'Digite o {i+1}° número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]} e os valores impares são {lista[1]}')
