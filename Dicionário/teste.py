dicionario = {}
while True:
    keys = str(input("Digite a chave: "))
    dicionario[keys] = str(input("Digite os valores: "))
    saida = str(input("Deseja continuar?[S/N] "))
    if saida in "Nn":
        break
print(dicionario)