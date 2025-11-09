registrations_list = []
employee_names_list = []
salaries_list = []
net_salaries_list = []
number_of_dependents_list = []
gender_list = []
employee_age_list = []
employees_time_list = []

minimum_salary = 1320.00
year_of_foundation = 2000
current_year = 2025
minimum_year = 1960
inss_discount = 0.12

for n in range(1, 21):

    valid_employee_registration_number = False
    while not valid_employee_registration_number:
        employee_registration_number = input("Digite a sua matrícula (6 dígitos): ")
        if not (employee_registration_number.isdigit() and len(employee_registration_number) == 6):
            print("Matrícula inválida, deve conter 6 dígitos numéricos.")
        elif employee_registration_number in registrations_list:
            print("Matrícula já cadastrada.")
        else:
            registrations_list.append(employee_registration_number)
            valid_employee_registration_number = True

    valid_employee_name = False
    while not valid_employee_name:
        employee_name = input("Digite o seu nome completo: ")
        if not employee_name.replace(" ", "").isalpha():
            print("Nome inválido, use apenas letras e espaços.")
        elif employee_name in employee_names_list:
            print("Nome já cadastrado.")
        else:
            employee_names_list.append(employee_name)
            valid_employee_name = True

    valid_gender = False
    while not valid_gender:
        gender = input("Sexo (M para masculino ou F para feminino): ").upper()
        if gender not in ("M", "F"):
            print("Informe 'M' para masculino ou 'F' para feminino.")
        else:
            gender_list.append(gender)
            valid_gender = True

    valid_gross_salary = False
    while not valid_gross_salary:
        try:
            gross_salary = float(input("Digite seu salário bruto: "))
            if gross_salary < minimum_salary:
                print(f"O salário deve ser igual ou maior do que o salário mínimo ({minimum_salary}).")
            else:
                salaries_list.append(gross_salary)
                valid_gross_salary = True
        except ValueError:
            print("Salário inválido, digite um número válido.")

    valid_number_of_dependents = False
    while not valid_number_of_dependents:
        try:
            number_of_dependents = int(input("Quantos dependentes você tem? "))
            if number_of_dependents < 0:
                print("O número de dependentes não pode ser negativo.")
            else:
                number_of_dependents_list.append(number_of_dependents)
                valid_number_of_dependents = True
        except ValueError:
            print("Digite um número inteiro válido.")

    valid_year_of_birth = False
    while not valid_year_of_birth:
        try:
            year_of_birth = int(input("Ano de nascimento: "))
            age = current_year - year_of_birth
            if year_of_birth < minimum_year or year_of_birth > current_year - 18:
                print(f"Ano de nascimento deve ser entre {minimum_year} e {current_year - 18}.")
            else:
                employee_age_list.append(age)
                valid_year_of_birth = True
        except ValueError:
            print("Digite um ano válido.")

    valid_year_of_entry = False
    while not valid_year_of_entry:
        try:
            year_of_entry = int(input("Ano de ingresso na empresa: "))
            if year_of_entry < year_of_foundation or year_of_entry > current_year:
                print(f"Ano de ingresso deve estar entre {year_of_foundation} e {current_year}.")
            else:
                employees_time_list.append(current_year - year_of_entry)
                valid_year_of_entry = True
        except ValueError:
            print("Digite um ano válido.")

for i in range(len(salaries_list)):
    full_salary = salaries_list[i]
    dependents = number_of_dependents_list[i]

    d_inss = full_salary * inss_discount

    if full_salary <= 1500:
        d_ir = 0
    elif full_salary <= 2700:
        d_ir = full_salary * 0.15
    elif full_salary <= 4700:
        d_ir = full_salary * 0.275
    else:
        d_ir = full_salary * 0.35

    family_salary = dependents * 14

    salary_deducted = full_salary - d_inss - d_ir + family_salary
    net_salaries_list.append(salary_deducted)

longer_time = max(employees_time_list)
longest_employees = []
for i in range(len(employees_time_list)):
    if employees_time_list[i] == longer_time:
        longest_employees.append(employee_names_list[i])

women_salaries = []
women_names = []
for i in range(len(gender_list)):
    if gender_list[i] == "F":
        women_salaries.append(net_salaries_list[i])
        women_names.append(employee_names_list[i])

if len(women_salaries) > 0:
    higgest_salary_woman = max(women_salaries)
    women_with_higgest_salaries = []
    for i in range(len(women_salaries)):
        if women_salaries[i] == higgest_salary_woman:
            women_with_higgest_salaries.append(women_names[i])
else:
    higgest_salary_woman = 0
    women_with_higgest_salaries = []

young_men_1700 = 0
total_of_men = 0
for i in range(len(gender_list)):
    if gender_list[i] == "M":
        total_of_men += 1
        if employee_age_list[i] < 27 and net_salaries_list[i] < 1700:
            young_men_1700 += 1
if total_of_men > 0:
    percentange_young_men_1700 = (young_men_1700 / total_of_men) * 100
else:
    percentange_young_men_1700 = 0

sum_discount_salary = sum(net_salaries_list)

women_with_more_than_3_depedents = 0
total_women = 0
for i in range(len(gender_list)):
    if gender_list[i] == "F":
        total_women += 1
        if number_of_dependents_list[i] > 3:
            women_with_more_than_3_depedents += 1
if total_women > 0:
    percentage_of_women_with_more_than_3_depedents = (women_with_more_than_3_depedents / total_women) * 100
else:
    percentage_of_women_with_more_than_3_depedents = 0

print("\nResultados:")

print("a) Funcionário(s) mais antigo(s):")
for f in longest_employees:
    print(f" - {f}")

if women_with_higgest_salaries:
    print(f"\nb) Funcionária(s) com maior salário líquido de R${higgest_salary_woman:.2f}:")
    for f in women_with_higgest_salaries:
        print(f" - {f}")
else:
    print("\nb) Nenhuma funcionária cadastrada.")

print(f"\nc) Porcentagem de homens com menos de 27 anos e salário líquido menor que R$1700: {percentange_young_men_1700:.2f}%")

print(f"\nd) Soma total dos salários líquidos de todos os funcionários: R${sum_discount_salary:.2f}")

print(f"\ne) Porcentagem de funcionárias com mais de 3 dependentes: {percentage_of_women_with_more_than_3_depedents:.2f}%")
