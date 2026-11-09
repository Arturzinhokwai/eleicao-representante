votos_Ana=0
votos_Caua=0
votos_Matheus=0
votos_Mariane=0
votos_brancos=0

opcao=0

while opcao != 6:
    print("\n===== ELEICAO DO REPRESENTANTE =====")
    print("1 - Votar em Ana")
    print("2 - Votar em Caua")
    print("3 - Votar em Matheus")
    print("3 - Votar em Mariane")
    print("4 - Votar em branco")
    print("5 - Consultar resultado parcial")
    print("6 - Encerrar votacao")

    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        votos_Ana += 1
        print("Voto em Ana Registrado")

    elif opcao == 2:
        votos_Caua += 1
        print("Voto em Caua Registrado")

    elif opcao == 3:
        votos_Matheus += 1
        print("Voto em Mathesu Registrado")

    elif opcao == 4:
        votos_Mariane+=1
        print("Voto em Mariane Registrado")

    elif opcao == 5:
        votos_brancos+=1
        print("Voto em Branco Registrado")


    elif opcao == 6:
        print("\nEncerrando a votacao...")

    else:
        print("opcao invalida! Tente novamente.")


total=votos_Ana+votos_Caua+votos_Mariane+votos_brancos+votos_Matheus

print("\n ======Resultado Final======")
print("votos em Ana",votos_Ana)
print("votos em Caua",votos_Caua)
print("votos em Matheus",votos_Matheus)
print("votos em Mariane",votos_Mariane)
print("votos em Branco",votos_brancos)
print("votos Totais",total)


if votos_Ana > votos_Caua and votos_Ana > votos_Matheus and votos_Ana > votos_Mariane:
    print("Candidato vencedor: Ana")

elif votos_Caua > votos_Matheus and votos_Caua > votos_Mariane and votos_Caua > votos_Ana:
    print("Candidato vencedor: Caua")

elif votos_Matheus > votos_Caua and votos_Matheus > votos_Mariane and votos_Matheus > votos_Ana:
    print("Candidato vencedor: Matheus")

elif votos_Mariane > votos_Caua and votos_Mariane > votos_Ana and votos_Mariane > votos_Matheus:
    print("Candidato vencedor: Mariane")

else:
    maior = votos_Ana

    if votos_Mariane > maior:
        maior = votos_Mariane

    if votos_Caua > maior:
        maior = votos_Caua

    if votos_Matheus > maior:
        maior = votos_Matheus

    if votos_Mariane == maior:
        print("A candidata Mariane esta empatada na maior quantidade de votos!")

    if votos_Caua == maior:
        print("O candidato Caua esta empatado na maior quantidade de votos!")

    if votos_Matheus == maior:
        print("O candidato Matheus esta empatado na maior quantidade de votos!")

    if votos_Ana == maior:
        print("A candidata Ana esta empatada na maior quantidade de votos!")

    print("HOUVE UM EMPATE ENTRE OS CANDIDATOS MAIS VOTADOS!!")

print("Voração encerrada!")






























