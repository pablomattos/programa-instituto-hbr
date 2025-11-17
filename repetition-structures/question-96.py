# Escreva um algoritmo para ler as notas da 1a. e 2aa avaliações de um aluno,
# calcular e imprimir a média. Faça com que o algoritmo só aceite notas válidas( uma nota válida
# deve pertencer ao interval [0,10]. Cada nota deve ser validada separadamente. Deve ser impressa
# a mensagem "Nota inválida"caso a nota informada não pertença ao intervalo [0,10].
# [Dados de entrada]  [Saída esperada] -1 (nota 1)
# Nota inválida
# 11 (nota 1)
# 9 (nota 1)
# 12 (nota 2)
# 10 (nota 2)
# Nota inválida
# Nota inválida
# 9.5 (média)

notes_list = []
count = 0

while count < 2:
    try:
        note = float(input(f"Digite a nota {count + 1}: "))

        if 0 <= note <= 10:
            notes_list.append(note)
            count += 1
        else:
            print("Nota inválida")

    except ValueError:
        print("Entrada inválida. Digite uma nota ( 0 a 10): ")

average_notes = sum(notes_list) / 2
print(f"{average_notes:.1f} (média)")
