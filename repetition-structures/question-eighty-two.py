# Faça um algoritmo que lê 10 valores, calcula a média dos valores pares que estão no
# interval entre 20 e 50. Ao final o programa deverá mostrar a média do valores, quantos valores
# estão no interval entre 20 e 50 e quantos não estão

even_numbers = []
quantity_even_numbers = 0
values_within_range = 0
values_out_of_range = 0
all_values = 0

try:
    list_of_ten_numbers = input().split()

    if len(list_of_ten_numbers) == 10:

        for number in list_of_ten_numbers:
            number = int(number)
            all_values += number

            if number >= 20 and number <= 50:
                values_within_range += 1

                if number % 2 == 0:
                    even_numbers.append(number)
                    quantity_even_numbers += 1

            else:
                values_out_of_range +=1
        if quantity_even_numbers > 0:
            average_of_even_values = sum(even_numbers) / quantity_even_numbers

        else:
            average_of_even_values = 0

        average_of_all_values = all_values / 10


    else:
        raise ValueError("You entered the wrong quantity of numbers ")

except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Average of even values between 20 and 50:  {average_of_even_values}")
    print(f"Average of all values: {average_of_all_values}")
    print(f"Quantity of values within range: {values_within_range}")
    print(f"Quantity of values out of range: {values_out_of_range}")