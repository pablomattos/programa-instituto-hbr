# Elabore um algoritmo que pede ao usuário números até que seja digitado um
# valor negativo, ao final do programa mostre os seguintes resultados:
# a) o maior valor
# b) o menor valor
# c) a soma dos valores pares
# d) a média dos valores ímpares

list_of_numbers = []
number = 0

while number >= 0:
    try:
        number = int(input("Enter a number (negative to stop): "))
        if number >= 0:
            list_of_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer number.")

if list_of_numbers:
    even_sum = sum(n for n in list_of_numbers if n % 2 == 0)
    odd_values = [n for n in list_of_numbers if n % 2 != 0]
    odd_avg = sum(odd_values) / len(odd_values) if odd_values else 0

    print(f"\nThe highest value is: {max(list_of_numbers)}")
    print(f"The lowest value is: {min(list_of_numbers)}")
    print(f"The sum of even values is: {even_sum}")
    print(f"The average of odd values is: {odd_avg:.2f}")
else:
    print("No positive numbers entered.")
