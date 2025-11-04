grenais = 0
gremio_wins = 0
inter_wins = 0
draws = 0
proceed = True

while proceed:

    valid_gremio = False
    while not valid_gremio:
        try:
            gremio_goals = int(input("Número de gols do Grêmio: "))
            valid_gremio = True
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para os gols do Grêmio.")

    valid_inter = False
    while not valid_inter:
        try:
            inter_goals = int(input("Número de gols do Inter: "))
            valid_inter = True
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para os gols do Inter.")

    grenais += 1

    if inter_goals > gremio_goals:
        print("O time do Inter venceu")
        inter_wins += 1
    elif gremio_goals > inter_goals:
        print("O time do Grêmio venceu")
        gremio_wins += 1
    else:
        print("EMPATE")
        draws += 1

    valid_response = False
    while not valid_response:
        new_game = input("Novo GRENAL 1.Sim 2.Não? ")
        if new_game == "1":
            valid_response = True
            proceed = True
        elif new_game == "2":
            valid_response = True
            proceed = False
        else:
            print("Valor inválido. Tente novamente.")

if inter_wins > gremio_wins:
    winner = "O Inter venceu o maior número de GRENAIS"
elif gremio_wins > inter_wins:
    winner = "O Grêmio venceu o maior número de GRENAIS"
else:
    winner = "Não houve vencedor"

print(f"\nQuantos GRENAIS fizeram parte da estatística: {grenais}")
print(f"O número de vitórias do Inter: {inter_wins}")
print(f"O número de vitórias do Grêmio: {gremio_wins}")
print(f"O número de empates: {draws}")
print(f"Resultado final: {winner}")
