number_of_classes = 18
min_frequency = int(number_of_classes * 0.75)

enrollment_list = []
final_grades = []
status_list = []

fail_count = 0
high_grade_count = 0
fail_due_frequency_count = 0

for _ in range(1, 21):
    valid_registration_number = False
    while not valid_registration_number:
        registration_number = input("Número de matrícula: ")
        if not (registration_number.isdigit() and len(registration_number) == 6):
            print("Matrícula inválida. Deve conter exatamente 6 dígitos numéricos. Tente novamente.")
        elif registration_number in enrollment_list:
            print("Número de matrícula já foi inserido. Informe outro.")
        else:
            enrollment_list.append(registration_number)
            valid_registration_number = True

    notes = []
    for n in range(1, 6):
        valid_note = False
        while not valid_note:
            try:
                note = float(input(f"Digite a {n}ª nota: "))
                if 0 <= note <= 10:
                    notes.append(note)
                    valid_note = True
                else:
                    print("Nota inválida. Deve ser um número entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

    valid_frequency = False
    while not valid_frequency:
        try:
            frequency = int(input(f"Número de aulas frequentadas (0 a {number_of_classes}): "))
            if 0 <= frequency <= number_of_classes:
                valid_frequency = True
            else:
                print(f"Entrada inválida. Deve ser entre 0 e {number_of_classes}.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

    average_of_notes = sum(notes) / 5

    approved = average_of_notes >= 6 and frequency >= min_frequency
    status = "Aprovado" if approved else "Reprovado"
    final_grades.append(average_of_notes)
    status_list.append((registration_number, average_of_notes, status))

    if not approved:
        fail_count += 1
        if frequency < min_frequency:
            fail_due_frequency_count += 1
    if average_of_notes > 9:
        high_grade_count += 1

print("\nResultados finais dos alunos:")
for registration, final_note, status in status_list:
    print(f"Matrícula: {registration} | Nota final: {final_note:.2f} | {status}")

highest_note = max(final_grades)
lowest_note = min(final_grades)
percentange_of_failed_attendance = (fail_due_frequency_count / 20) * 100

print(f"\nb) Maior nota final da turma: {highest_note:.2f}")
print(f"c) Menor nota final da turma: {lowest_note:.2f}")
print(f"d) Total de alunos reprovados: {fail_count}")
print(f"e) Total de alunos com nota final superior a 9: {high_grade_count}")
print(f"f) Percentual de alunos reprovados por frequência abaixo de {min_frequency} aulas: {percentange_of_failed_attendance:.2f}%")
