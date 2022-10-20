# Slovníky, JSON

## Slovníky

### 1

```py
kurz = {
    'nazev': 'Úvod do programování',
    'lektor': 'Martin Podloucký',
    'konani': [
        {
            'misto': 'T-Mobile',
            'koucove': [
                'Dan Vrátil',
                'Filip Kopecký',
                'Martina Nemčoková'
            ],
            'ucastnic': 30
        },
        {
            'misto': 'MSD IT',
            'koucove': [
                'Dan Vrátil',
                'Zuzana Tučková',
                'Martina Nemčoková'
            ],
            'ucastnic': 25
        },
        {
            'misto': 'Škoda DigiLab',
            'koucove': [
                'Dan Vrátil',
                'Filip Kopecký',
                'Kateřina Kalášková'
            ],
            'ucastnic': 41
        }
    ]
}

# Vypište na výstup počet účastnic na posledním konání kurzu.
print(kurz["konani"][-1]["ucastnic"])
# Vypište na výstup jméno posledního kouče na prvním konání kurzu. (Beru první v lidské řeči, pokud máte na pozici 1, je to taky správně)
print(kurz["konani"][0]["koucove"][-1])
# Vypište na výstup celkový počet konání kurzu.
print(len(kurz["konani"]))
# Vypište na výstup všechna místa, na kterých se kurz konal. Použijte chroustání seznamů.
mista = [konani["misto"] for konani in kurz["konani"]]
print(mista)
```

### 2

Super nápady jsou na [Slacku](https://czechitasdadata.slack.com/archives/C03V6R3280Y/p1665509907038449).

### 3

```py
recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

ceny_list = [ing[-1] for ing in recept['ingredience']]
ceny_rozd = [cena.split(" ") for cena in ceny_list]
ceny_stringy = [cena[0] for cena in ceny_rozd]
ceny_cisla = [float(cena) for cena in ceny_stringy]
celkova_cena = sum(ceny_cisla)
zaokrouhlena_cena = round(celkova_cena)
print(zaokrouhlena_cena)
```

## Formát JSON

### 1

```py
import requests
import json
response = requests.get("http://api.kodim.cz/python-data/people")
data = json.loads(response.text)

# První řešení - tady počítám s tím, že vím, že možnosti jsou pouze 2 a na každou si vytvořím proměnnou
# a vlastní chroustání nebo větev v podmínce
males = len([g for g in gender if g == "Male"])
females = len([g for g in gender if g == "Female"])
print("Počet mužů je", males, "a počet žen", females)
males = 0
females = 0
for p in data:
    if p["gender"] == "Female":
        females = females + 1
    else:
        males = males + 1
print("Počet mužů je", males, "a počet žen", females)


# Vytvořím si slovník, na začátku mám u obou pohlaví 0.
# Názvy pohlaví musím mít přesně tak, jak jsou v datech!
results = {"Female": 0, "Male": 0}
# Cyklem projdu seznam
for p in data:
    # Načtu si aktuální pohlaví
    # Pohlaví využiju jako klíč - je to klíč hodnoty ve slovníku, kterou chci upravit
    gender = p["gender"]
    # Nyní zvýším hodnotu ve slovníku pro příslušný klíč o 1 - našel jsem jednoho dalšího muže nebo jednu další ženu
    results[gender] = results[gender] + 1
print("Počet mužů je", results["Male"], "a počet žen", results["Female"])

"""
Toto je ještě obecnější varianta, kterou bych použil, pokud by se mi nechtělo vytvářet
ručně prázdný slovník. U 2 pohlaví je to jednoduché, ale u dat s více možnostmi
by to bylo pracné. Začnu tím, že vytvořím prázdný slovník.
"""
results = {}
# Cyklem projdu seznam
for p in data:
    gender = p["gender"]
    """
    Nyní nepoužiju hranatou závorku, ale metodu "get". Tato funkce vrátí hodnotu podle klíče.
    Můžu jí ale předat i druhý parametr (zde 0). Pokud metoda klíč ve slovníku nenajde, tak vrátí
    hodnotu, která je zadaná jako druhý parametr (zde 0). Čtení pomocí hranatých závorek by zde
    skončilo nulou!
    Tj. pokud vkládám do slovníku nové pohlaví, metoda get vrátí 0 (což je v pořádku, nové pohlaví nemá žádný záznam).
    Pak už standardně přičtu 1 a vložím hodnotu do slovníku.
    """
    results[gender] = results.get(gender, 0) + 1
print(results)
```

### 2

Příklad spuštění programu:

```
python program.py 2404
```

```py
import requests
import json
import sys
from datetime import date
response = requests.get('http://svatky.adresa.info/json')
svatek_dnes = json.loads(response.text)
print(svatek_dnes[0]['name'])

DDMM = sys.argv[1]
response = requests.get('https://svatky.adresa.info/json?date=' + DDMM)
svatek = json.loads(response.text)
print(svatek[0]['name'])
```
