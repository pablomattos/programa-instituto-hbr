final_grades = []
approved_students = []
failed_students = 0
exam_students = 0
grades_above_eight = 0

valid_number_of_students = False
while not valid_number_of_students:
    try:
        number_of_students = int(input("Número de alunos da turma: "))
        if number_of_students > 0:
            valid_number_of_students = True
        else:
            print("Digite um número positivo de alunos da turma.")
    except ValueError:
        print("Valor inválido, digite um número inteiro positivo.")

for student in range(number_of_students):
    notes = []
    student = int(student)
    student += 1
    print(f"Aluno {student}: ")
    for n in range(1, 3):
        valid_note = False
        while not valid_note:
            try:
                note = float(input(f"Digite a {n}ª nota: "))
                if 0 <= note <= 10:
                    notes.append(note)
                    valid_note = True
                else:
                    print("Nota inválida. Deve ser uma nota entre 0 e 10: ")
            except ValueError:
                print("Entrada inválida. Digite uma nota válida: ")

    final_grade = sum(notes) / 2
    final_grades.append(final_grade)

    if final_grade >= 6:
        approved_students.append(final_grade)
    elif 5 <= final_grade < 6:
        exam_students += 1
    else:
        failed_students += 1

    if final_grade > 8:
        grades_above_eight += 1

if len(approved_students) > 0:
    average_approved = sum(approved_students) / len(approved_students)
else:
    average_approved = 0

percentage_failed = (failed_students / number_of_students) * 100
highest_grade = max(final_grades) if final_grades else 0

print(f"a) Número de alunos aprovados: {len(approved_students)}")
print(f"b) Número de alunos reprovados: {failed_students}")
print(f"c) Número de alunos em exame: {exam_students}")
print(f"d) Média das notas finais dos alunos aprovados: {average_approved:.2f}")
print(f"e) Percentual de alunos reprovados: {percentage_failed:.2f}%")
print(f"f) A maior nota da turma: {highest_grade:.2f}")
print(f"g) Número de alunos com média superior a 8: {grades_above_eight}")
