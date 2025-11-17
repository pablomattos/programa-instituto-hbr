state_abbreviations = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

total_vehicles = 0
total_traffic_accidents = 0
total_traffic_accidents_in_rs = 0
number_of_cities_with_traffic_accidents_in_rs = 0

max_accidents = -1
min_accidents = float('inf')
city_code_max_accidents = None
city_code_min_accidents = None

for code in range(1, 201):

    valid_code = False
    while not valid_code:
        try:
            city_code = int(input(f"Código da cidade ({code}): "))
            if city_code != code:
                raise ValueError(f"Código inválido. Deve ser o código da cidade {code}.")
            valid_code = True
        except ValueError as e:
            print(f"Error: {e}")

    valid_abbreviation = False
    while not valid_abbreviation:
        try:
            state_abbreviation = input("Estado (sigla): ").strip().upper()
            if state_abbreviation not in state_abbreviations:
                raise ValueError("Sigla inválida. Insira uma sigla de estado válida.")
            valid_abbreviation = True
        except ValueError as e:
            print(f"Error: {e}")

    valid_vehicles = False
    while not valid_vehicles:
        try:
            number_of_passenger_vehicles = int(input("Número de veículos de passeio em 2018: "))
            if number_of_passenger_vehicles < 0:
                raise ValueError("Número de veículos não pode ser negativo.")
            valid_vehicles = True
        except ValueError as e:
            print(f"Error: {e}")

    valid_accidents = False
    while not valid_accidents:
        try:
            number_of_traffic_accidents = int(input("Número de acidentes de trânsito com vítimas em 2018: "))
            if number_of_traffic_accidents < 0:
                raise ValueError("Número de acidentes não pode ser negativo.")
            valid_accidents = True
        except ValueError as e:
            print(f"Error: {e}")

    total_vehicles += number_of_passenger_vehicles
    total_traffic_accidents += number_of_traffic_accidents

    if number_of_traffic_accidents > max_accidents:
        max_accidents = number_of_traffic_accidents
        city_code_max_accidents = code
    if number_of_traffic_accidents < min_accidents:
        min_accidents = number_of_traffic_accidents
        city_code_min_accidents = code

    if state_abbreviation == "RS":
        total_traffic_accidents_in_rs += number_of_traffic_accidents
        number_of_cities_with_traffic_accidents_in_rs += 1

average_vehicles = total_vehicles / 200
average_accidents_rs = (total_traffic_accidents_in_rs / number_of_cities_with_traffic_accidents_in_rs
                        if number_of_cities_with_traffic_accidents_in_rs > 0 else 0)

print(f"\nMaior índice de acidentes: {max_accidents}, Cidade código: {city_code_max_accidents}")
print(f"Menor índice de acidentes: {min_accidents}, Cidade código: {city_code_min_accidents}")
print(f"Média de veículos nas cidades brasileiras: {average_vehicles:.2f}")
print(f"Média de acidentes com vítimas nas cidades do RS: {average_accidents_rs:.2f}")
