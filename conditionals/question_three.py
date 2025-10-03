# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores
# digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados
# foram negativos
negative_numbers = 0
positive_numbers = 0
even_numbers = 0
odd_numbers = 0

number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())
number_five = int(input())

if number_one % 2 == 0:
    even_numbers += 1

else:
    odd_numbers += 1

if number_one > 0:
    positive_numbers += 1

elif number_one < 0:
    negative_numbers += 1

if number_two % 2 == 0:
    even_numbers += 1

else:
    odd_numbers += 1

if number_two > 0:
    positive_numbers += 1

elif number_two < 0:
    negative_numbers += 1

if number_three % 2 == 0:
    even_numbers += 1

else:
    odd_numbers += 1

if number_three > 0:
    positive_numbers += 1

elif number_three < 0:
    negative_numbers += 1

if number_four % 2 == 0:
    even_numbers += 1

else:
    odd_numbers += 1

if number_four > 0:
    positive_numbers += 1

elif number_four < 0:
    negative_numbers += 1

if number_five % 2 == 0:
    even_numbers += 1

else:
    odd_numbers += 1

if number_five > 0:
    positive_numbers += 1

elif number_five < 0:
    negative_numbers += 1


print(f"{even_numbers} valor(es) par(es)")
print(f"{odd_numbers} valor(es) ímpar(es)")
print(f"{positive_numbers} valor(es) positivo(s)")
print(f"{negative_numbers} valor(es) negativo(s)")





