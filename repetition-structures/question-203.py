valid_minimum_salary = False
while not valid_minimum_salary:
    try:
        minimum_salary = float(input("Valor do salário mínimo: "))
        if minimum_salary >= 1320.00:
            valid_minimum_salary = True
        else:
            print("O valor do salário mínimo deve ser igual ou maior do que 1320.")
    except ValueError:
        print("Valor inválido, digite um número válido.")

number_of_hours_worked_list = []
number_of_dependents_of_the_employees_list = []
number_of_overtime_list = []

valid_hours = True
while valid_hours:
    try:
        hours = int(input("Digite as horas trabalhadas do funcionário (ou -1 para encerrar): "))
        if hours == -1:
            valid_hours = False
        elif hours <= 0:
            print("Digite uma quantidade de horas maior que zero ou -1 para sair.")
        else:
            number_of_hours_worked_list.append(hours)
    except ValueError:
        print("Valor inválido, digite um número inteiro.")

for i in range(len(number_of_hours_worked_list)):
    valid_dependents = False
    while not valid_dependents:
        try:
            dependents = int(input(f"Número de dependentes do funcionário {i+1}: "))
            if dependents < 0:
                print("Número de dependentes não pode ser negativo.")
            else:
                number_of_dependents_of_the_employees_list.append(dependents)
                valid_dependents = True
        except ValueError:
            print("Valor inválido, digite um número inteiro.")

for i in range(len(number_of_hours_worked_list)):
    valid_overtime = False
    while not valid_overtime:
        try:
            overtime = int(input(f"Número de horas extras do funcionário {i+1}: "))
            if overtime < 0:
                print("Número de horas-extras não pode ser negativa.")
            else:
                number_of_overtime_list.append(overtime)
                valid_overtime = True
        except ValueError:
            print("Valor inválido, digite um número inteiro.")

value_of_hour_worked = minimum_salary / 10
value_of_overtime = value_of_hour_worked * 1.5

print("\nVencimentos dos funcionários:")
print(70 * "-")

for i in range(len(number_of_hours_worked_list)):
    monthly_salary = number_of_hours_worked_list[i] * value_of_hour_worked
    dependents_value = number_of_dependents_of_the_employees_list[i] * 32
    overtime_value = number_of_overtime_list[i] * value_of_overtime
    gross_salary = monthly_salary + dependents_value + overtime_value

    if gross_salary <= 900:
        irrf = 0
    elif gross_salary <= 1500:
        irrf = gross_salary * 0.10
    else:
        irrf = gross_salary * 0.20

    net_salary = gross_salary - irrf

    if net_salary <= 900:
        bonus = 100
    else:
        bonus = 50

    final_salary = net_salary + bonus

    print(f"Funcionário {i+1}:")
    print(f"  Salário do mês: R$ {monthly_salary:.2f}")
    print(f"  Salário bruto: R$ {gross_salary:.2f}")
    print(f"  IRRF descontado: R$ {irrf:.2f}")
    print(f"  Salário líquido: R$ {net_salary:.2f}")
    print(f"  Gratificação: R$ {bonus:.2f}")
    print(f"  Salário a receber: R$ {final_salary:.2f}")
    print(70 * "-")
