## Podmínky pro řízení běhu

### 1

```py
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
if b == 0:
    print("Nulou nelze dělit!")
else:
    vysledek = a / b
    vysledek = round(vysledek, 3)
    print(vysledek)
```

### 2

```py
import sys
nazev_souboru = sys.argv[1]
if nazev_souboru.endswith(".csv"):
  print(nazev_souboru)
else:
  print("Tento soubor nelze zpracovat")
```

### 3

```py
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
if a > b:
  print(a)
else:
  print(b)
```

### 4

```py
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a > b:
  nejvetsi = a
else:
  nejvetsi = b

if nejvetsi < c:
  nejvetsi = c

print(nejvetsi)
```

## Cyklus FOR


### 1

```py
import sys
cisla = sys.argv[1:]
# a
for cislo in cisla:
    print(cislo)
# b
for cislo in cisla:
    cislo = int(cislo)
    print(cislo, cislo * (- 1))
# c
for cislo in cisla:
    cislo = int(cislo)
    if cislo > 0:
        print(cislo)
# d
for cislo in cisla:
    cislo = int(cislo)
    if cislo > 0:
        print(cislo)
    else:
        print(cislo * (-1))
```

### 2

První program vypíše sudá čísla ze seznamu.

Druhý program namísto jmen, která začínají na "p", vypíše "pako", ostatní jména v seznamu vypíše normálně.
