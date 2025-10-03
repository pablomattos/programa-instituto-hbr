#  Leia 5 valores Inteiros. Ordene os valores e exiba os tanto na ordem crescente quanto na ordem
# decrescente.

number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())
number_five = int(input())


list_in_ascending_order = 0
list_in_descending_order = 0

if number_one < number_two:
    list_in_descending_order = number_one, number_two

if number_two < number_three:
    list_in_ascending_order = number_one, number_two, number_three

