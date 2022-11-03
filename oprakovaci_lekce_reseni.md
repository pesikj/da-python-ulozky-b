## Soubor JSON

```py
import json
with open("people.json", encoding="utf-8") as soubor:
    people = json.load(soubor)
# Chci načíst data o uživatelce na začátku souboru
prvni_uzivatelka = people[0]
# Chci vypsat jméno a příjmení první uživatelky
print(prvni_uzivatelka["first_name"], prvni_uzivatelka["last_name"])
# Jméno poslední kamarádky
seznam_kamaradek = prvni_uzivatelka["friends"].split(", ")
# Podívám se, zde má uživatelka korespondenční adresu
# Tj. kontroluji, zda má slovník prvni_uzivatelka klíč mail_address
if "mail_address" in prvni_uzivatelka:
    # Pokud ho má, můžu si ho uložit
    adresa = prvni_uzivatelka["mail_address"]
    # Rozdělím adresu podle řádků
    adresa = adresa.split("\n")
    # Chci mesto - je na druhém řádku po PSČ
    # PSČ a mezery vždy zaberou znaky na pozicích 0 až 6, město začíná na 7
    mesto = adresa[1][7:]
else:
    # Pokud uživatel nemá korespondenční adresu, použiju trvalé bydliště
    adresa = prvni_uzivatelka["permanent_address"]
    adresa = adresa.split("\n")
    mesto = adresa[1][7:]

# Chci vypsat jména a příjmení všech uživatelů do souboru
vystup = []
for uzivatel in people:
    # Řetězec: first_name,last_name
    radek = uzivatel["first_name"] + "," + uzivatel["last_name"] + "\n"
    # Řetězec vložím do seznamu vystup
    vystup.append(radek)
with open("people.csv", mode="w", encoding="utf-8") as soubor:
    soubor.writelines(vystup)
```

## Soubor TSV

```py
with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()
radky = [radek.split("\t") for radek in radky]
# attacker_1 na pozici 5
utocnici = [radek[5] for radek in radky]

"""
Níže je jeden ze způsobů, jak spočítat útočníky. Vezmu všechny čtyři sloupce, kde mohou být útočníci,
a načtu si jejich jména. U sloupců s druhými, třetími a čtvrtými útočníky vynechávám prázdné řetězce,
protože útočník může být třeba jen jeden.
"""
utocnici_1 = [radek[5] for radek in radky[1:]]
utocnici_2 = [radek[6] for radek in radky[1:] if len(radek) > 0]
utocnici_3 = [radek[7] for radek in radky[1:] if len(radek) > 0]
utocnici_4 = [radek[8] for radek in radky[1:] if len(radek) > 0]
# Vytvořím si slovník, kam si budu dělat "čárky" za každý útok
utocnici_slovnik = {}
for utocnik in utocnici_1:
    """
    Mohl bych použít podmínku ke kontrole, jestli už jsem na rod někdy narazil a mám ho ve slovníku.
    Alternativa je využití metody get.
    Pokud je klíč ve slovníku, vrátí get hodnotu pro příslušný klíč.
    Pokud tam není, vrátí hodnotu, která je zadaná jako druhý parametr.
    Zde dává smysl 0, protože rod zatím neútočil, když není ve slovníků.
    """
    utocnici_slovnik[utocnik] = utocnici_slovnik.get(utocnik, 0) + 1
for utocnik in utocnici_2:
    utocnici_slovnik[utocnik] = utocnici_slovnik.get(utocnik, 0) + 1
for utocnik in utocnici_3:
    utocnici_slovnik[utocnik] = utocnici_slovnik.get(utocnik, 0) + 1
for utocnik in utocnici_4:
    utocnici_slovnik[utocnik] = utocnici_slovnik.get(utocnik, 0) + 1
print(utocnici_slovnik)

"""
Nyní si vytvoříme seznam bitev, kde méně početná armáda porazila tu početnější
"""

mensi_armada_vyhrala = []
for radek in radky[1:]:
    """
    Nyní řeším, zda mám velikost obou armád.
    Pokud ano, převedu obě velikosti na číslo a porovnám, zda
    v bitvě vyhrála početně slabší armáda
    """
    if len(radek[17]) > 0 and len(radek[18]):
        attacker_size = float(radek[17])
        defender_size = float(radek[18])
        # Pokud byl útočník početně slabší a vyhrál, uložím si název bitvy
        if attacker_size < defender_size and radek[13] == "win":
            mensi_armada_vyhrala.append(radek[0])
        # Pokud byl útočník početně silnější a prohrál, uložím si název bitvy
        if attacker_size > defender_size and radek[13] == "loss":
            mensi_armada_vyhrala.append(radek[0])
print(mensi_armada_vyhrala)
```
