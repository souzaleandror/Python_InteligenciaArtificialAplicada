
lista_de_resenhas = []

with open('desafio_final.txt', 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

print(lista_de_resenhas)