answer = "sim"
gender_list = ["masculino", "feminino"]
eye_color_list = ["azuis", "verdes", "castanhos"]
hair_color_list = ["louros", "castanhos", "pretos"]

new_gender_list = []
new_eye_color_list = []
new_hair_color_list = []
age_list = []
height_list = []
weight_list = []

number_of_participants = 0

try:
    while answer.lower() == "sim":
        valid_input_gender = False
        valid_input_eye = False
        valid_input_hair = False
        valid_input_age = False
        valid_input_height = False
        valid_input_weight = False

        while not valid_input_gender:
            gender = input("Sexo (masculino ou feminino): ").lower()
            if gender in gender_list:
                new_gender_list.append(gender)
                valid_input_gender = True
            else:
                print("Sexo inválido, digite masculino ou feminino.")

        while not valid_input_eye:
            eye_color = input("Cor dos olhos (azuis, verdes, castanhos): ").lower()
            if eye_color in eye_color_list:
                new_eye_color_list.append(eye_color)
                valid_input_eye = True
            else:
                print("Cor dos olhos inválida, digite azuis, verdes ou castanhos.")

        while not valid_input_hair:
            hair_color = input("Cor dos cabelos (louros, castanhos, pretos): ").lower()
            if hair_color in hair_color_list:
                new_hair_color_list.append(hair_color)
                valid_input_hair = True
            else:
                print("Cor dos cabelos inválida, digite louros, castanhos ou pretos.")

        while not valid_input_age:
            try:
                age = int(input("Idade: "))
                if 0 < age < 200:
                    age_list.append(age)
                    valid_input_age = True
                else:
                    print("Valor de idade inválida, digite entre 1 e 200.")
            except ValueError:
                print("Digite um número inteiro válido para idade.")

        while not valid_input_height:
            try:
                height = int(input("Altura (em cm): "))
                if 0 < height < 300:
                    height_list.append(height)
                    valid_input_height = True
                else:
                    print("Altura inválida, digite entre 1 e 300 cm.")
            except ValueError:
                print("Digite um número inteiro válido para altura.")

        while not valid_input_weight:
            try:
                weight = int(input("Peso (em kg): "))
                if 0 < weight < 300:
                    weight_list.append(weight)
                    valid_input_weight = True
                else:
                    print("Peso inválido, digite entre 1 e 300 kg.")
            except ValueError:
                print("Digite um número inteiro válido para peso.")

        number_of_participants += 1

        answer_valid = False
        while not answer_valid:
            answer = input("Deseja continuar? (sim/não): ").lower()
            if answer in ["sim", "não"]:
                answer_valid = True
            else:
                print("Resposta inválida. Digite apenas 'sim' ou 'não'.")

    average_age = sum(age_list) / number_of_participants
    average_height = sum(height_list) / number_of_participants
    average_weight = sum(weight_list) / number_of_participants

    percentage_female = (sum(1 for g in new_gender_list if g == "feminino") / number_of_participants) * 100
    percentage_male = (sum(1 for g in new_gender_list if g == "masculino") / number_of_participants) * 100

    count_green_eyes = sum(1 for e in new_eye_color_list if e == "verdes")
    count_blond_hair = sum(1 for h in new_hair_color_list if h == "louros")

except Exception as e:
    print(f"Error: {e}")

else:
    print("\n===== RESULTADOS =====")
    print(f"Participantes: {number_of_participants}")
    print(f"Média de idade: {average_age:.1f} anos")
    print(f"Média de altura: {average_height:.1f} cm")
    print(f"Média de peso: {average_weight:.1f} kg")
    print(f"Porcentagem de mulheres: {percentage_female:.1f}%")
    print(f"Porcentagem de homens: {percentage_male:.1f}%")
    print(f"Pessoas com olhos verdes: {count_green_eyes}")
    print(f"Pessoas com cabelos louros: {count_blond_hair}")

