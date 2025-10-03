#Questão 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import math

side_of_the_square = 0
double_the_value_of_the_area = 0

print("Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
side_of_the_square = float(input("Digite o valor do lado de um quadrado: "))

double_the_value_of_the_area = 2 * math.pow(side_of_the_square, 2)

print("O dobro da área do quadrado de lado de", side_of_the_square,"m é igual a: ", double_the_value_of_the_area,"m²")
