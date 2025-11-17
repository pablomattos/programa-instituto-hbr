old_salaries = [30000, 20000, 15000, 6000, 3500, 3000]
code_positions = [101, 102, 103, 104, 105, 106]
positions = ["Diretor", "Gerente", "Engenheiro", "Técnico", "Auxiliar", "Administrativo"]
percentage_increase = [1.1, 1.15, 1.2, 1.3, 1.35, 1.4]

valid_continue_the_system = True
max_salary_limit = max(old_salaries)
minimum_salary = 1320.00

while valid_continue_the_system:
    valid_employee_salary = False
    while not valid_employee_salary:
        try:
            employee_salary = float(input("Salário do funcionário: "))
            if employee_salary < minimum_salary:
                print(f"Digite um salário igual ou maior que o salário mínimo: R$ {minimum_salary:.2f}.")
            elif employee_salary > max_salary_limit:
                print(f"Salário digitado não pode ser maior que o maior salário permitido: R$ {max_salary_limit:.2f}.")
            else:
                valid_employee_salary = True
        except ValueError:
            print("Valor inválido, digite um valor numérico válido.")

    valid_employees_position = False
    index = None
    job_title = None
    applies_fixed_increase = False

    while not valid_employees_position:
        employees_position_code_str = input(
            "Código do cargo do funcionário (ex: 101) ou deixe vazio para cargo fora da lista: ").strip()

        if employees_position_code_str == "":
            valid_cargo_name = False
            while not valid_cargo_name:
                nome_cargo = input("Cargo não listado, por favor digite o nome do cargo: ").strip()
                if nome_cargo.replace(" ", "").isalpha():
                    job_title = nome_cargo
                    valid_cargo_name = True
                    valid_employees_position = True
                    applies_fixed_increase = True
                else:
                    print("Entrada inválida, digite um nome de cargo válido, sem números ou caracteres especiais.")
        elif employees_position_code_str.isdigit():
            employees_position_code = int(employees_position_code_str)
            if employees_position_code in code_positions:
                index = code_positions.index(employees_position_code)
                salary_for_position = old_salaries[index]
                job_title = positions[index]

                if abs(employee_salary - salary_for_position) > 0.01:
                    print(
                        f"Alerta: salário informado (R$ {employee_salary:.2f}) difere do salário padrão para {job_title} (R$ {salary_for_position:.2f}).")
                    print(
                        "Por favor, informe o código do cargo correto para o salário digitado ou digite um cargo fora da lista.")
                else:
                    valid_employees_position = True
                    applies_fixed_increase = False
            else:
                print("Código do cargo não listado, tente novamente ou deixe vazio para informar cargo fora da lista.")
        else:
            print("Entrada inválida, digite apenas números para o código do cargo ou deixe vazio.")

    if applies_fixed_increase:
        new_salary = employee_salary * 1.5
    else:
        percentage_increase_in_salary = percentage_increase[index]
        new_salary = employee_salary * percentage_increase_in_salary

    salary_difference = new_salary - employee_salary

    print(f"\nCargo do funcionário: {job_title}")
    print(f"Salário antigo: R$ {employee_salary:.2f}")
    print(f"Novo salário: R$ {new_salary:.2f}")
    print(f"Diferença de salário: R$ {salary_difference:.2f}\n")

    valid_input = False
    while not valid_input:
        continue_the_system = input(
            "Deseja digitar novamente os dados? (digite S para sim ou N para não): ").strip().upper()
        if continue_the_system == "S":
            valid_input = True
            valid_continue_the_system = True
        elif continue_the_system == "N":
            valid_input = True
            valid_continue_the_system = False
        else:
            print("Valor inválido, digite S para sim ou N para não.")
