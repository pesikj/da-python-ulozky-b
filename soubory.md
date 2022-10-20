## Soubory: čtení a zápis

### 1

```py
with open('data/pasazeri.txt', encoding='utf-8') as vstup:
  radky = vstup.readlines()

radky = [radek.split() for radek in radky]
radky = [[dvojice.split(",") for dvojice in radek] for radek in radky]
radky = [[[int(dvojice[0]), int(dvojice[1])] for dvojice in radek] for radek in radky]
tam_prvni_den = sum([dvojice[0] for dvojice in radky[0]])
zpet_prvni_den = sum([dvojice[1] for dvojice in radky[0]])
print(f"Tam jelo {tam_prvni_den} pasažérů a zpět {zpet_prvni_den} pasažérů.")

tam_cely_tyden = sum([sum([dvojice[0] for dvojice in radek]) for radek in radky])
zpet_cely_tyden = sum([sum([dvojice[1] for dvojice in radek]) for radek in radky])
print(f"Za celý týden jelo {tam_cely_tyden} pasažérů a zpět {zpet_cely_tyden} pasažérů.")
```

### 2

```py
with open('data/znamky.txt', encoding='utf-8') as vstup:
  radky = vstup.readlines()

radky = [radek.split("\t") for radek in radky]
zahlavi = radky[0]

radky = [[znamka.replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D").replace("5", "F") for znamka in radek] for radek in radky[1:]]
radky = [zahlavi] + radky
print(radky)
radky = ["\t".join(radek) for radek in radky]
with open('data/znamky_upravene.txt', mode='w', encoding='utf-8') as vystup:
  vystup.writelines(radky)
```

### 3

```py
import random

barvy = ["kříže", "srdce", "piky", "káry"]
hodnoty = list(range(2, 11)) + ["kluk", "dáma", "král", "eso"]

karty = [[barvy[random.randint(0, len(barvy) - 1)], hodnoty[random.randint(0, len(hodnoty) - 1)]] for _ in range(0, 4)]
hodnoty = [str(karta[1]).replace("kluk", "10").replace("dáma", "10").replace("král", "10").replace("eso", "1") for karta in karty]
hodnoty = [int(hodnota) for hodnota in hodnoty]
print(karty)
print(sum(hodnoty))
```

### 4

```py
import random

with open('data/karty.txt', encoding='utf-8') as vstup:
  radky = vstup.readlines()

# Zamíchám balíček a beru první 4 karty
random.shuffle(radky)
karty = radky[:4]
karty = [karta.strip().split() for karta in karty]
# Zkopírováno z minulé úložky, pouze upraven index
hodnoty = [str(karta[0]).replace("kluk", "10").replace("dáma", "10").replace("král", "10").replace("eso", "1") for karta in karty]
hodnoty = [int(hodnota) for hodnota in hodnoty]

print(karty)
print(sum(hodnoty))
```

