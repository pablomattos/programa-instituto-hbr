monthly_fee = {
    1: 300,
    2: 400,
    3: 500,
    4: 600
}

total_collected = 0
values_families = []

running = True

while running:
    valid_number = False
    while not valid_number:
        try:
            number_of_children = int(input("Digite o número de filhos (0 para encerrar): "))
            if number_of_children == 0:
                running = False
                valid_number = True
            else:
                if number_of_children < 0:
                    print("Número de filhos deve ser positivo ou 0 para encerrar.")
                else:
                    valid_number = True
        except ValueError:
            print("Por favor, digite um número válido.")

    if running:
        family_value = 0
        current_son = 1

        while current_son <= number_of_children:
            print(f"Filho {current_son}:")
            valid_level = False
            while not valid_level:
                try:
                    level_of_education = int(input(
                        "  Digite o nível de escolaridade (1-pré-escola, 2-1o ciclo, 3-2o ciclo, 4-ensino médio): "))
                    if level_of_education in monthly_fee:
                        valid_level = True
                    else:
                        print("Nível inválido! Digite um valor entre 1 e 4.")
                except ValueError:
                    print("Valor inválido! Digite um número entre 1 e 4.")

            base_value = monthly_fee[level_of_education]
            discount = 0.1 * (current_son - 1) if current_son > 1 else 0
            if discount > 0.9:
                discount = 0.9
            discounted_price = base_value * (1 - discount)
            family_value += discounted_price
            current_son += 1

        values_families.append(family_value)
        total_collected += family_value

index = 1
for value in values_families:
    print(f"Valor total a pagar pela família {index}: R$ {value:.2f}")
    index += 1

print(f"Total arrecadado pela escola: R$ {total_collected:.2f}")
