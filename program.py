pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
pocty_dni = [f"{x}\n" for x in pocty_dni]
with open("kalendar.txt", mode="w", encoding="utf-8") as soubor:
    soubor.writelines(pocty_dni)

nazvy_mesicu = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
vystup = [f"{nazvy_mesicu[i]}\t{pocty_dni[i]}" for i in range(12)]
with open("kalendar_b.txt", mode="w", encoding="utf-8") as soubor:
    soubor.writelines(vystup)

with open("kalendar_c.txt", mode="w", encoding="utf-8") as soubor:
    soubor.writelines(["měsíc\tpočet dní\n"])
with open("kalendar_c.txt", mode="a", encoding="utf-8") as soubor:
    soubor.writelines(vystup)
print(list(zip(nazvy_mesicu, pocty_dni)))