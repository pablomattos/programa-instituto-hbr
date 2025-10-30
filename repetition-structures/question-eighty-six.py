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
        quantity_of_numbers = int(input("How many numbers will you type? "))
        if quantity_of_numbers > 0:
            valid_quantity = True
        else:
            print("Enter a quantity greater than 0.")
    except ValueError:
        print("Please enter a valid integer.")

proceed = True
while proceed:
    try:
        list_of_numbers = input(f"Enter {quantity_of_numbers} numbers: ").split()

        if len(list_of_numbers) == quantity_of_numbers:
            new_list_of_numbers = []
            all_valid = True

            for number in list_of_numbers:
                try:
                    new_list_of_numbers.append(int(number))
                except ValueError:
                    print("Please enter only valid integers.")
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

                print(f"\nHighest value: {highest_value}")
                print(f"Lowest value: {lowest_value}")
                print(f"Sum of values: {sum_of_values}")
                print(f"Average of values: {average_of_values:.2f}")
                print(f"Quantity of values greater than 20: {number_of_values_greater_than_20}")
                print(f"Percent of values greater than 10: {percent_of_values_greater_than_10:.2f}%")
                print(f"Average of values between 10 and 100: {average_of_values_between_10_and_100:.2f}")

                proceed = False
            else:
                print("Try entering the numbers again.")

        else:
            print(f"You entered {len(list_of_numbers)} numbers, you need to enter {quantity_of_numbers} numbers!")

    except Exception as e:
        print(f"Error: {e}")
