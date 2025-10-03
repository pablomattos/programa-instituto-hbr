#  Leia 5 valores Inteiros. Ordene os valores e exiba os tanto na ordem crescente quanto na ordem
# decrescente.

number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())
number_five = int(input())


if number_one > number_two:
    number_one, number_two = number_two, number_one

if number_two > number_three:
    number_two, number_three = number_three, number_two

if number_three > number_four:
    number_three, number_four = number_four, number_three

if number_four > number_five:
    number_four, number_five = number_five, number_four

if number_one > number_two:
    number_one, number_two = number_two, number_one

if number_two > number_three:
    number_two, number_three = number_three, number_two

if number_three > number_four:
    number_three, number_four = number_four, number_three

if number_one > number_two:
    number_one, number_two = number_two, number_one

if number_two > number_three:
    number_two, number_three = number_three, number_two

if number_one > number_two:
    number_one, number_two = number_two, number_one

print(number_one, number_two, number_three, number_four, number_five)
print(number_five, number_four, number_three, number_two, number_one)


