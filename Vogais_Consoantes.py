vogais = ('aeiou')
consoantes = ('bcdfghjklmnpqrstvwyxz')
cont_vogais = 0
cont_conso = 0
frase = input("Digite uma frase (Não utilize acentos): ").lower()
for i in vogais:
    for c in frase:
            if i == c:
                cont_vogais += 1 
for i in consoantes:
    for c in frase:
            if i == c:
                cont_conso += 1
    
print(f"Você digitou {cont_vogais} vogais e {cont_conso} consoantes")
