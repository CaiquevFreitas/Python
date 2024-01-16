temp = list()
boletim = list()
num_alunos = 0
while True: 
    temp.append(str(input("Digite um nome: ")))
    temp.append(float(input("Digite a primeira nota: ")))
    temp.append(float(input("Digite a segunda nota: ")))
    temp.append((temp[1] + temp[2])/2)
    boletim.append(temp[:])
    temp.clear()
    fim = str(input("Deseja continuar? [S/N]: ")).upper()
    if 'N' in fim:
        break
num_alunos = len(boletim)
print("="*30)
print("\tBOLETIM")
print("="*30)
for i in range(0,num_alunos):
    print(f'Nome: {boletim[i][0]} | Média: {boletim[i][3]}')
