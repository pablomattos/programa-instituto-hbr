list_of_volleyball_players = []
valid_class_code = False
additional_value = ''

while not valid_class_code:
    try:
        players_base_salary = float(input("Digite o valor do salário do jogador: "))
        if players_base_salary <= 5000:
            print("Salário está abaixo da categoria, digite um valor igual ou maior do que 5000: ")
    except ValueError:
        print("Valor inválido, digite um valor igual ou maior do que 5000: ")
    try:
        class_code = int(input("Digite o código da classe do jogador: "))
        if not 1 <= class_code <= 7:
            valid_class_code = False
        else:
            valid_class_code = True
            match class_code:
                case 1:
                    level = "excelente"
                    additional_value = 1

                case 2:
                    level = "bom"
                    additional_value = 0.8

                case 3:
                    level = "médio"
                    additional_value = 0.5

                case 4:
                    level = "regular"
                    additional_value = 0.3

                case 5:
                    level = "precisa treinar mais"
                    additional_value = 0.1

                case 6:
                    level = "te cuida"
                    additional_value = 0.05

                case 7:
                    level = "tsktsk"
                    additional_value = 0
                case _:
                    print("Classe inválida")
            list_of_volleyball_players.append(players_base_salary, level, additional_value)

    except ValueError:
        print("Valor inválido, digite um número inteiro 1 a 7, ou qualquer outro para excerrar: ")









