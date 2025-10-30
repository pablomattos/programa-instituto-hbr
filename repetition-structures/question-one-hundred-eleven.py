favorite_club_list = [1, 2, 3, 0]
city_of_origin_list = [0, 1]

gremio_club = []
internacional_club = []
others_club = []
people_interviewed = 0
porto_alegre_others = 0

valid_input_club = True

while valid_input_club:
    print()
    club = int(input("Clube de preferência (1-Grêmio; 2-Internacional; 3-Outros; 0-Sair): "))

    try:
        if club == 0:
            valid_input_club = False

        # Se o clube for válido e diferente de 0, continua com a coleta
        elif club in [1, 2, 3]:
            city = int(input("Cidade de origem (0-Porto Alegre; 1-Outras): "))

            if city in city_of_origin_list:
                people_interviewed += 1

                if club == 1:
                    gremio_club.append(city)
                elif club == 2:
                    internacional_club.append(city)
                elif club == 3:
                    others_club.append(city)
                    if city == 0:
                        porto_alegre_others += 1
            else:
                print("Valor inválido. Digite (0-Porto Alegre; 1-Outras).")

        else:
            print("Valor inválido. Digite 1-Grêmio; 2-Internacional; 3-Outros ou 0 para sair.")

    except:

print("\n===== RESULTADOS =====")
print(f"Torcedores do Grêmio: {len(gremio_club)}")
print(f"Torcedores do Internacional: {len(internacional_club)}")
print(f"Torcedores de Outros clubes: {len(others_club)}")
print(f"Pessoas de Porto Alegre que torcem por 'Outros': {porto_alegre_others}")
print(f"Total de pessoas entrevistadas: {people_interviewed}")
