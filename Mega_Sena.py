import random
import time
qtd_jogos = int(input("Quantos jogos deseja fazer? "))
temp = list()
jogos = list()

for i in range (0,qtd_jogos):
    for p in range (0,6):
        temp.append(random.randint(1,60))
    jogos.append(temp[:])
    temp.clear()

print("="*40)
print("\tJOGOS DA MEGA SENA")
print("="*40)
for i in range (0, qtd_jogos):
    print(f'{i+1}° jogo: {jogos[i]}')
    time.sleep(1)
