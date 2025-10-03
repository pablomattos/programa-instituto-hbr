# Assim, para melhor se organizarem para as próximas viagens, eles pediram que você faça um
# aplicativo para celular que, dada a hora de saída, tempo de viagem e o fuso do destino com relação
# à origem, você informe a hora de chegada de cada vôo no destino

departure_time = int(input())
travel_time = int(input())
destination_zone = int(input())
arrival_time = 0
day = 24
if (departure_time >= 0 or departure_time <= 23) and (travel_time >= 1 or travel_time <= 12) and (destination_zone >= -5 or destination_zone <= 5):
    if day  < (departure_time + travel_time) :
        arrival_time = (departure_time + travel_time) - day + destination_zone

    elif (travel_time + destination_zone) < departure_time:
        arrival_time = day + (travel_time + destination_zone)
        
    else:
        arrival_time = departure_time + travel_time + destination_zone

else:
    print("Dados inválidos")
print(arrival_time)

