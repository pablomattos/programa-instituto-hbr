#ENTRADA
# A entrada é composta por seis linhas, nessa ordem:
# a primeira linha contém o identificador do cliente;
# #a segunda linha contém a leitura anterior do medidor em kWh (inteiro);
# a terceira linha contém a leitura atual do medidor em kWh (inteiro);
# #a quarta linha contém a tarifa da bandeira em reais por kWh (número real);
# #a quinta linha contém o custo de distribuição em reais por kWh (número real); #
# e a sexta linha contém o valor da iluminação pública em reais (número real).#

customer_identifier = input()
previous_meter_reading = int(input())
current_meter_reading = int(input())
flag_tariff_in_reais_per_kWh = float(input())
distribution_cost_in_reais_per_kWh = float(input())
value_of_public_lighting = float(input())


electricity_consumption = current_meter_reading - previous_meter_reading
value_of_electrical_energy = electricity_consumption * flag_tariff_in_reais_per_kWh
value_of_energy_distribution = electricity_consumption * distribution_cost_in_reais_per_kWh
total_electricity_bill = value_of_electrical_energy + value_of_energy_distribution + value_of_public_lighting


print("CLIENTE ", customer_identifier,": CONSUMO ", electricity_consumption ," KWH")
print("ENERGIA: R$ ",f"{value_of_electrical_energy:.2f}")
print("DISTRIBUICAO: R$ ",f"{value_of_energy_distribution:.2f}")
print("ILUMINACAO: R$", f"{value_of_public_lighting:.2f}")
print("TOTAL: R$ ", f"{total_electricity_bill:.2f}")