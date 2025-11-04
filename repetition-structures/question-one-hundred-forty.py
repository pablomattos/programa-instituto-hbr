grades_of_all_students = []

for count_student in range(1, 11):
    valid_input = False
    while not valid_input:
        try:
            print(f"Aluno {count_student} - digite 5 notas separadas por espaço (0 a 10):")
            notes = input().split()
            if len(notes) != 5:
                raise ValueError("Digite exatamente 5 notas!")
            float_notes = [float(n) for n in notes]

            valid_notes = True
            for note in float_notes:
                if note < 0 or note > 10:
                    valid_notes = False
                    raise ValueError("Cada nota deve estar entre 0 e 10!")

            if valid_notes:
                grades_of_all_students.append(float_notes)
                valid_input = True

        except Exception as e:
            print("Erro:", e)

print("\nResultados:")

count_student = 1
for notes in grades_of_all_students:
    average_of_notes = sum(notes) / 5
    print(f"Aluno {count_student} - Média: {average_of_notes:.2f}")
    if 0 <= average_of_notes <= 2:
        print("Situação: Nota PÉSSIMA")
    elif 2 < average_of_notes <= 4:
        print("Situação: Nota MUITO RUIM")
    elif 4 < average_of_notes <= 6:
        print("Situação: Nota de quem NÃO ESTUDOU O SUFICIENTE")
    elif 6 < average_of_notes <= 7:
        print("Situação: Nota NO LIMITE")
    elif 7 < average_of_notes <= 8:
        print("Situação: Nota BOA, pode melhorar")
    elif 8 < average_of_notes <= 9:
        print("Situação: Nota MUITO BOA!")
    elif 9 < average_of_notes <= 10:
        print("Situação: Nota na DISPUTA PELA COXINHA! :-)")
    else:
        print("Nota inválida!")
    count_student += 1
