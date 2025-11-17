candidate_one = 0
candidate_two = 0
candidate_three = 0
candidate_four = 0
null_vote = 0
white_vote = 0

for e in range(1, 31):
    valid_vote = False
    while not valid_vote:
        try:
            vote = int(input("Escolha seu candidato: 1,2,3 ou 4, 5 para voto nulo e 6 para voto em branco: "))
            if vote == 1:
                candidate_one += 1
                valid_vote = True
            elif vote == 2:
                candidate_two += 1
                valid_vote = True
            elif vote == 3:
                candidate_three += 1
                valid_vote = True
            elif vote == 4:
                candidate_four += 1
                valid_vote = True
            elif vote == 5:
                null_vote += 1
                valid_vote = True
            elif vote == 6:
                white_vote += 1
                valid_vote = True
            else:
                print("Digite somente os números de 1 a 6 para o seu voto.")
        except ValueError:
            print("Valor inválido, digite um voto de 1 a 6.")

percentage_of_null_vote = (null_vote / 30) * 100
percentage_of_white_vote = (white_vote / 30) * 100

print("--------------RESULTADOS--------------")
print(f"a) total de votos do candidato 1: {candidate_one}")
print(f"b) total de votos do candidato 2: {candidate_two}")
print(f"c) total de votos do candidato 3: {candidate_three}")
print(f"d) total de votos do candidato 4: {candidate_four}")
print(f"e) total de votos nulos: {null_vote}")
print(f"f) total de votos em branco: {white_vote}")
print(f"g) percentual dos votos nulos sobre o total: {percentage_of_null_vote:.2f}%")
print(f"h) percentual dos votos em branco sobre o total: {percentage_of_white_vote:.2f}%")
