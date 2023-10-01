import os
#Cadastro clientes
nome = []
cpf = []
email = []
telefone = []

continuar = 'S'
while continuar =='S':
    nome.append(input("Digite o nome completo: ").title())
    cpf.append(input("Informe o cpf(sem pontos e traços): "))
    email.append(input("Informe o email: "))
    telefone.append(input("Informe o telefone: "))
    continuar = input("Deseja continuar S/N: ").upper()

#Busca dos dados dos clientes
os.system('clear')
buscar = input("Digite o nome ou cpf do cliente que deseja buscar: ").title()
for indice in range(0, len(nome)):
    if buscar == nome[indice] or buscar == cpf[indice]:
        print("Nome: ", nome[indice])
        print("Cpf: ", cpf[indice])
        print("email: ", email[indice])
        print("telefone: ", telefone[indice])