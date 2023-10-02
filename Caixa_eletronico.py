print("="*45)
print("\tBem vindo ao Banco do Brasil")
print("="*45)
valor = int(input("Informe o valor que deseja sacar: R$"))

total = valor
ced = [100, 50, 20, 10, 5, 2]
totalced = 0 
for i in ced:
    while total >= i:
        total -= i 
        totalced += 1
    if total < i and totalced > 0:
        print("Total de {} cédula(s) de R${}".format(totalced, i))
        totalced = 0
    if total == 0:
        break
print("="*45)
print("\tCaixa Encerrado")
print("="*45)  
