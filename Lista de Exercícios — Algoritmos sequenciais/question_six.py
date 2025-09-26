#Questão 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

radius_value = 0
area_of_the_circle = 0

print("Programa que pede o raio de um círculo, calcula e mostre sua área.")
radius_value = float(input("Digite o valor do raio de um círculo: "))

area_of_the_circle = math.pi * (math.pow(radius_value, 2))

print("A área do círculo de raio ", radius_value, "m, é igual a ", round(area_of_the_circle, 2),"m²")   
