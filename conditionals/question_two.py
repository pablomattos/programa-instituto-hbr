# Faça um programa em Python 3 que leia o tipo de combustível (codificado da seguinte forma: A -
# Álcool, G - Gasolina) e o número de litros vendidos, calcule e mostre o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 6,10 o preço do litro do álcool é R$ 5,75

fuel_type = input()
quantity_of_liters_of_fuel = float(input())
total_to_pay = 0
total_to_pay_with_discount = 0

if fuel_type.upper() == "A" and quantity_of_liters_of_fuel > 0:
    total_to_pay = quantity_of_liters_of_fuel * 5.75

    if quantity_of_liters_of_fuel <= 20:
        total_to_pay_with_discount = total_to_pay - (total_to_pay * 0.055)
        print(f"Valor a pagar: R${total_to_pay_with_discount:.2f}")

    else:
        total_to_pay_with_discount = total_to_pay - (total_to_pay * 0.08)
        print(f"Valor a pagar: R${total_to_pay_with_discount:.2f}")


elif fuel_type.upper() == "G" and quantity_of_liters_of_fuel > 0:
    total_to_pay = quantity_of_liters_of_fuel * 6.10

    if quantity_of_liters_of_fuel <= 20:
        total_to_pay_with_discount = total_to_pay - (total_to_pay * 0.035)
        print(f"Valor a pagar: R${total_to_pay_with_discount:.2f}")

    else:
        total_to_pay_with_discount = total_to_pay - (total_to_pay * 0.10)
        print(f"Valor a pagar: R${total_to_pay_with_discount:.2f}")

elif (fuel_type.upper() == "A" or fuel_type.upper() == "G") and quantity_of_liters_of_fuel < 0:
    print("QUANTIDADE INVÁLIDA")

elif (fuel_type.upper() != "A" or fuel_type.upper() != "G") and quantity_of_liters_of_fuel < 0:
    print("CÓDIGO INVÁLIDO")
    print("QUANTIDADE INVÁLIDA")

elif (fuel_type.upper() != "A" or fuel_type.upper() != "G") and quantity_of_liters_of_fuel > 0:
    print("CÓDIGO INVÁLIDO")

