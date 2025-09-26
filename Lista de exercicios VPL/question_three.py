import re

team_name = input()
normalized_team_name = team_name.title()
name_contains_FC = team_name.upper().find("FC") != -1
name_starts_with_s = team_name.startswith("S")
name_ends_with_ense = team_name.upper().endswith("ENSE")
name_contains_clube = team_name.upper().find("CLUBE") != -1
name_contains_atletico = team_name.upper().find("ATLETICO") != -1
valid_name = bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", team_name))
short_name = len(team_name.replace(" ", "")) < 10

emphasis = ( ( team_name.upper().find("FC") or team_name.upper().find("CLUBE") or team_name.upper().find("GREMIO" )) != -1 and  short_name == False)

print("NOME_NORMALIZADO: ", normalized_team_name )
print("TEM_FC: ",name_contains_FC )
print("COMECA_COM_S: ",name_starts_with_s )
print("TERMINA_COM_ENSE: ",name_ends_with_ense )
print("TEM_CLUBE: ", name_contains_clube )
print("TEM_ATLETICO: ", name_contains_atletico )
print("NOME_CURTO: ", short_name )
print("NOME_VALIDO: ", valid_name )
print("DESTAQUE: ", emphasis)
