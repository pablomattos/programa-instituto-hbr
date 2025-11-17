#  O Grêmio estudantil da escola resolveu fazer uma pesquisa com os alunos para
# descobrir quantos alunos tinham usado o Xerox no último mês. Desenvolva um programa que
# determine:
# a) total de alunos que fizeram uso do xerox
# b) percentual de alunos que utilizaram menos de 5 vezes
# c) percentual de alunos que utilizaram entre 5 e 10 vezes
# d) percentual de alunos que utilizaram mais de 10 vezes
# e) quantidade de vezes que os alunos utilizaram
# f) a média de utilização
# g) a maior e a menor quantidade utilizada no mês

students_who_used_the_photocopier = []
valid_use_photocopier = True
while valid_use_photocopier:
    valid_registration_number = False
    try:
        while not valid_registration_number:
            registration_number = input("Digite a sua matrícula para utilizar o xerox: ")
            if not (registration_number.isdigit() and len(registration_number) == 6):
                print("Matrícula inválida, deve conter 6 dígitos: ")
            else:
                valid_registration_number = True
                students_who_used_the_photocopier.append(registration_number)
    except ValueError:
        print("Valor inválido, digite 6 dígitos: ")

    valid_input = False
    while not valid_input:
        try:
            continue_the_month = input("Digite S para continuar o mês ou N para finalizar: ").strip().upper()
            if continue_the_month == "S":
                valid_input = True
                valid_use_photocopier = True
            elif continue_the_month == "N":
                valid_input = True
                valid_use_photocopier = False
            else:
                print("Letra inválida, digite S ou N: ")
        except ValueError:
            print("Valor inválido, digite S ou N:")

usage_count_per_student = {}
for registration in students_who_used_the_photocopier:
    if registration in usage_count_per_student:
        usage_count_per_student[registration] += 1
    else:
        usage_count_per_student[registration] = 1

total_students = len(usage_count_per_student)

less_than_five = 0
between_five_and_ten = 0
more_than_ten = 0
for times in usage_count_per_student.values():
    if times < 5:
        less_than_five += 1
    elif 5 <= times <= 10:
        between_five_and_ten += 1
    else:
        more_than_ten += 1

percent_less_than_five = (less_than_five / total_students) * 100
percent_between_five_and_ten = (between_five_and_ten / total_students) * 100
percent_more_than_ten = (more_than_ten / total_students) * 100

sum_of_uses = 0
for value in usage_count_per_student.values():
    sum_of_uses += value
average = 0
if total_students > 0:
    average = sum_of_uses / total_students
else:
    average = 0

if usage_count_per_student:
    higgest = max(usage_count_per_student.values())
    lowest = min(usage_count_per_student.values())

else:
    higgest, lowest = 0, 0

print(70*"-")
print(f"Total de alunos: {total_students}")
print(f"Percentual de alunos que usaram < 5 vezes: {percent_less_than_five:.2f}%")
print(f"Percentual de alunos que usaram entre 5 e 10 vezes: {percent_between_five_and_ten:.2f}%")
print(f"Percentual de alunos que usaram > 10 vezes: {percent_more_than_ten:.2f}%")
print("Matrícula | Quantidade de vezes")
for reg, amount in usage_count_per_student.items():
    print(f"{reg}    | {amount}")
print(f"Média de utilização: {average:.2f}")
print(f"Maior utilização: {higgest} | Menor utilização: {lowest}")






