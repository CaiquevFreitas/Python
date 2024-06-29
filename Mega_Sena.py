import random
import time
qtd_jogos = int(input("Quantos jogos deseja fazer? "))
temp = list()
jogos = list()

for i in range (0,qtd_jogos):
    while len(temp) < 6:
        num = random.randint(1,60)
        if num not in temp:
            temp.append(num)
    jogos.append(temp[:])
    temp.clear()

print("="*40)
print("\tJOGOS DA MEGA SENA")
print("="*40)
for i in range (0, qtd_jogos):
    print(f'{i+1}° jogo: {jogos[i]}')
    time.sleep(1)
