# 1

```py
import sys

spravne_heslo = "Czechitas"
if sys.argv[2] == spravne_heslo:
    print("Přístup povolen")
else:
    print("Přístup odepřen")
```

Příklady spuštění programu:

```
python program.py test test
python program.py test Czechitas
```

# 2

```py
import sys

kurz_koruna = 25.03
kurz_euro = 1.02

castka = int(sys.argv[2])

if sys.argv[1] == "czk":
    print(castka / kurz_koruna)
elif sys.argv[1] == "eur":
    print(castka / kurz_euro)
# Další měny by šly přidat stejným způsobem
```

# 3

```py
with open("zustatky.txt", encoding="utf-8") as soubor:
    zustatky = soubor.readlines()

cislo_radku = 1
for radek in zustatky:
    zustatek = float(radek) * 1.025
    if zustatek > 0:
        print(cislo_radku, zustatek)
    cislo_radku += 1
```

# 5

```py
# Příklad vstupního seznamu
seznam = [1, 2, 3, 4, 9]

# Funkce range je vysvětlená v povinných úložkách k lekci První programy
for i in range(1, len(seznam)):
    if seznam[i-1] >= seznam[i]:
        print("Seznam není seřazen vzestupně.")
        exit()
print("Seznam je seřazen vzestupně.")
```

# 6

```py
import sys
znamky = sys.argv[1:]

# Je možné použít i proměnné a mít na každou známku proměnnou
# My použijeme seznam
# Na pozici 0 je počet jedniček, na pozici 1 počet dvojek atd
pocet_znamek = [0, 0, 0, 0, 0]

for znamka in znamky:
    znamka = int(znamka)
    # Musím od pozice odečíst 1, protože známky jsou od 1 a Python čísluje od 0
    pocet_znamek[znamka - 1] = pocet_znamek[znamka - 1] + 1
print("Vypisuji počet známek: ")

aktualni_znamka = 1
for pocet in pocet_znamek:
    print("Počet známek", aktualni_znamka, "je", pocet)
    aktualni_znamka = aktualni_znamka + 1
```

# 7

```py
import sys
cisla = sys.argv[1:]
"""
Neměli bychom nastavovat jako počáteční hodnotu 0, protože pak
by program nefungoval správně, pokud by všechna čísla na vstupu
byla záporná.
"""
maxium = float(cisla[0])
for cislo in cisla:
    cislo = float(cislo)
    if cislo > maxium:
        maxium = cislo
print(maxium)
```

# 8

```py
import sys
cisla = sys.argv[1:]

if float(cisla[0]) > float(cisla[1]):
    nejvyssi = float(cisla[0])
    druhe_nejvyssi = float(cisla[1])
else:
    nejvyssi = float(cisla[1])
    druhe_nejvyssi = float(cisla[0])

for cislo in cisla[2:]:
    cislo = float(cislo)
    if cislo > nejvyssi:
        druhe_nejvyssi = nejvyssi
        nejvyssi = cislo
    elif cislo > druhe_nejvyssi:
        druhe_nejvyssi = cislo
print(druhe_nejvyssi)
```

# 9

```py
import sys
poradi = int(sys.argv[1])

cisla = sys.argv[2:]
cisla = [int(cislo) for cislo in cisla]
nejvetsi_cisla = [cisla[0]]

for cislo in cisla[1:]:
    # Číslo je zatím největší, vložíme ho do seznamu největších čísel na začátek
    if cislo > nejvetsi_cisla[0]:
        nejvetsi_cisla = [cislo] + nejvetsi_cisla[:poradi-1]
        print(nejvetsi_cisla)
        # Číslo je již vložené do seznamu, můžeme tedy pokračovat dalším číslem
        continue
    for index in range(0, len(nejvetsi_cisla)):
        # Číslo je větší než některé z čísel v seznamu největších čísel, vložíme ho někam "doprostřed"
        if cislo > nejvetsi_cisla[index]:
            # Seznamy můžu "sčítat" podobně jako řetězce - součet seznamů znamená jejich "slepení" dohromady
            nejvetsi_cisla = nejvetsi_cisla[:index] + [cislo] + nejvetsi_cisla[index:poradi-1]
            print(nejvetsi_cisla)
            # Jakmile vložíme číslo do seznamu, přerušíme běh cyklu pomocí break
            # https://kodim.cz/kurzy/uvod-do-progr-2/bonusy/cykly-2/preruseni-cyklu
            break
    # Číslo je zatím nejmenší, ale seznam největších čísel je zatím příliš krátký, tak číslo vložíme nakonec
    if len(nejvetsi_cisla) < poradi and cislo not in nejvetsi_cisla:
        nejvetsi_cisla.append(cislo)
print(nejvetsi_cisla[-1])            
```
