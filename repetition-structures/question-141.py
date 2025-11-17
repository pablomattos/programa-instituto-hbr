# Faça um algoritmo que leia 3 notas obtidas por 5 alunos. Calcule a média de notas
# de todos os alunos usando a seguinte fórmula:
# Média por aluno (MA) = ( N1 + N2 + N3) / 3
# Média geral = (MA1 + MA2 +MA3 +MA4 +MA5) / 5

grades_of_all_students = []

for count_student in range(1, 6):
    valid_input = False
    while not valid_input:
        try:
            print(f"Aluno {count_student} - digite 3 notas separadas por espaço (0 a 10):")
            notes = input().split()
            if len(notes) != 3:
                raise ValueError("Digite exatamente 3 notas!")
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
sum_average_all_students = 0

for notes in grades_of_all_students:
    average_of_notes = sum(notes) / 3
    sum_average_all_students += average_of_notes

    print(f"Aluno {count_student} - Média: {average_of_notes:.2f}")
    if 9 <= average_of_notes <= 10:
        print("Conceito: A")
    elif 7.5 < average_of_notes <= 8.9:
        print("Conceito: B")
    elif 6 < average_of_notes <= 7.4:
        print("Conceito: C")
    elif 4 <= average_of_notes < 5.9:
        print("Conceito: D")
    elif  average_of_notes <= 4:
        print("Conceito: E")
    else:
        print("Nota inválida!")
    count_student += 1

average_all_students = sum_average_all_students / 5
print(f"Media geral: {average_all_students}")
