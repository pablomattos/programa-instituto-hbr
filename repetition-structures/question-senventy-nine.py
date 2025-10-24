#  Faça um programa que entra com 10 números e mostra quantos são pares e estão
# entre 10 e 50 ou 100 e 200.
even_between_10_and_50 = 0
even_between_100_and_200 = 0

try:
    list_of_ten_numbers = input().split()

    if len(list_of_ten_numbers) == 10:
        for number in list_of_ten_numbers:
            number = int(number)
            if number % 2 == 0 and number >= 10 and number <= 50:
                even_between_10_and_50 += 1

            if number % 2 == 0 and number >= 100 and number <= 200:
                even_between_100_and_200 += 1

    else:
        raise ValueError("You entered the wrong quantity of numbers ")

except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Quantidade de pares entre 10 e 50 {even_between_10_and_50}")
    print(f"Quantidade de pares entre 100 e 200 {even_between_100_and_200}")

