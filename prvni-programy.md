## První programy

Zadání úložek jsou [zde](https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/cteni-na-doma).

### 1

```py
import sys
casy = [12, 25, 64, 27, 15, 66, 128, 44]
casy_pod_hodinu = [cas for cas in casy if cas < 60]
print(casy_pod_hodinu)
casy_nad_hodinu = [cas - 60 for cas in casy if cas > 60]
print(casy_nad_hodinu)
casy = sys.argv[1:]
casy = [int(cas) for cas in casy]
print(casy)
```

### 2

```py
import sys
teplota_farenheit = int(sys.argv[1])
teplota_celsius = 5 * (teplota_farenheit - 32) / 9
print(teplota_celsius)
```

### 3

```py
import sys
retezec = sys.argv[1]
print(retezec.replace(" ", "_"))
```

### 4
#### a

```py
import random
hod = random.randint(1, 6)
print(hod)
```

#### b

```py
import random
import sys
pocet_hran = int(sys.argv[1])
hod = random.randint(1, pocet_hran)
print(hod)
```

#### c

```py
import random
import sys
pocet_hran = int(sys.argv[1])
pocet_hodu = int(sys.argv[2])
hody = [random.randint(1, pocet_hran) for _ in range(0, pocet_hodu)]
print(hody)
```

### 5

```py
import random

barvy = ["kříže", "srdce", "piky", "káry"]
hodnoty = list(range(2, 11)) + ["kluk", "dáma", "král", "eso"]
index_1 = random.randint(0, len(barvy) - 1)
index_2 = random.randint(0, len(hodnoty) - 1)
karta = f"{barvy[index_1]} {hodnoty[index_2]}"
print(karta)
```

### 6

```py
import sys

retezec = sys.argv[1]
pole = retezec.split("_")
pole = [slovo[0].upper() + slovo[1:] for slovo in pole]
retezec = "".join(pole)
retezec = retezec[0].lower() + retezec[1:]
print(retezec)

```

### 7

```py
import sys

retezec = sys.argv[1]
seznam = [x for x in retezec]
seznam = [("_" + x.lower()) * int(x == x.upper()) + x * int(x == x.lower()) for x in seznam]
print("".join(seznam))
```

Alternativní řešení:

```py
import sys
velbloudi_notace = (sys.argv[1])
sd = [velbloudi_notace[i] if velbloudi_notace[i] != velbloudi_notace[i].upper() else '_' + velbloudi_notace[i].lower() for i in range(len(velbloudi_notace))]
print(''.join(sd))
```
