notas = {}
while True:
    aluno = str(input("Digite o nome do Aluno: "))
    notas[aluno] = float(input("Digite a nota dele: "))
    media = notas.values()
    media = list(media)
    saida = str(input("Deseja continuar?[S/N] "))
    if saida in "Nn":
        print(notas)
        print(sum(media)/len(media))
        break
