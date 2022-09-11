## Poznámky k lekci

* Funkce round() v dokumentaci Pythonu https://docs.python.org/3/library/functions.html#round
* Přehled všech funkcí a modulů: https://docs.python.org/3/library/index.html
* Modul statistics: https://docs.python.org/3/library/statistics.html

## Doporučené úložky na doma

Zadání úložek jsou [zde](https://kodim.cz/kurzy/python-data/zaklady-programovani/hodnoty-promenne-funkce/cteni-na-doma).

### 1 - Délka filmu

```py
223 // 60
223 % 60
```

### 2 - Průměrné teploty
Vytvoření proměnné `radky`

```py
radky = [[2001, 7.8], [2002, 8.7], [2003, 8.2], [2004, 7.8], [2005, 7.7], [2006, 8.2], [2007, 9.1], [2008, 8.9], [2009, 8.4], [2010, 7.2]]
```

Vytvoření proměnné `sloupce`

```py
sloupce = [[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]]
```

#### 2 a

```py
radky[2][1]
```

#### 2 b

```py
radky[4][0]
```

#### 2 c

```py
radky[-1]
```

#### 2 d

```py
radky[2:]
```

#### 2 e

```py
radky[:2]
```

#### 2 f

```py
radky[4:8]
```

#### 2 g

```py
seznam_teplot = sloupce[1]
seznam_teplot.sort()
seznam_teplot
```

### 3 - Průměr
První řádek je pouze příklad

```py
seznam = [1, 2, 3, 4]
sum(seznam) / len(seznam)
```

## Volitelné úložky na doma

### 4

```py
30 ** 0.5
```

### 5

```py
s = [1, 2, 3, 4]
max(s) - min(s)
```

### 6

```py
s = [5, 9, 1, 0, 7, 3]
s.sort()
minimum = s[0]
maximum = s[-1]
```
### 7

```py
len(s) // 2
```

### 8

```py
(len(s) - 1) // 2
```
