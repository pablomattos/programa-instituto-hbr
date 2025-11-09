#  Elabore um algoritmo que depois de ler uma sequência de N números (N deve ser
# solicitado para o usuário), mostre os seguintes resultados:
# a) o maior valor
# b) o menor valor
# c) a soma dos valores
# d) a média dos valores
# e) quantos números maiores a 20
# f) a percentagem de valores maiores que 10
# g) a média dos valores entre 10 e 100

valid_quantity = False

while not valid_quantity:
    try:
        quantity_of_numbers = int(input("Quantos valores você vai digitar? "))
        if quantity_of_numbers > 0:
            valid_quantity = True
        else:
            print("Digite uma quantidade maior do que zero: ")
    except ValueError:
        print("Por favor, digite um valor inteiro: ")

proceed = True
while proceed:
    try:
        list_of_numbers = input(f"Digite {quantity_of_numbers} números: ").split()

        if len(list_of_numbers) == quantity_of_numbers:
            new_list_of_numbers = []
            all_valid = True

            for number in list_of_numbers:
                try:
                    new_list_of_numbers.append(int(number))
                except ValueError:
                    print("Por favor, digite somente valores inteiros: ")
                    all_valid = False

                    i = len(list_of_numbers)
                    while i < len(list_of_numbers):
                        i += 1

            if all_valid:
                highest_value = max(new_list_of_numbers)
                lowest_value = min(new_list_of_numbers)
                sum_of_values = sum(new_list_of_numbers)
                average_of_values = sum_of_values / len(new_list_of_numbers)

                greater_than_20 = [n for n in new_list_of_numbers if n > 20]
                number_of_values_greater_than_20 = len(greater_than_20)

                greater_than_10 = [n for n in new_list_of_numbers if n > 10]
                percent_of_values_greater_than_10 = (len(greater_than_10) * 100) / len(new_list_of_numbers)

                values_between_10_and_100 = [n for n in new_list_of_numbers if 10 <= n <= 100]
                if len(values_between_10_and_100) > 0:
                    average_of_values_between_10_and_100 = sum(values_between_10_and_100) / len(values_between_10_and_100)
                else:
                    average_of_values_between_10_and_100 = 0

                print(f"\nMaior valor: {highest_value}")
                print(f"Menor valor: {lowest_value}")
                print(f"Soma dos valores: {sum_of_values}")
                print(f"Média dos valores: {average_of_values:.2f}")
                print(f"Quantidade dos valores maior do que 20: {number_of_values_greater_than_20}")
                print(f"Percentual dos valores maiores do que 10: {percent_of_values_greater_than_10:.2f}%")
                print(f"Média dos valores entre 10 e 100: {average_of_values_between_10_and_100:.2f}")

                proceed = False
            else:
                print("Tente digitar os números novamente: ")

        else:
            print(f"Você digitou {len(list_of_numbers)} números, você precisa digitar {quantity_of_numbers} números: ")

    except Exception as e:
        print(f"Error: {e}")
