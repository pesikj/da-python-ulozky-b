# Soubor JSON

Máme data o lidech z imaginární sociální sítě, která jsou uložená v souboru `people.json`.

Příklad záznamu jednoho člověka

```
    {
        "first_name": "Otakar",
        "last_name": "Kučera",
        "birth_number": "155625/8341",
        "friends": "Hynek, Erik, Tomáš",
        "permanent_address": "Žherská 941\n383 98 Mikulášovice",
        "phone_number": "604 965 934",
        "mail_address": "Bajkalská 5\n411 22 Vimperk"
    }
```

Nejprve si vyzkoušíme, jak získat data o prvním uživateli. Vyřeš následující otázky, pracovat budeme s uživatele na začátku souboru:

- Vypiš jméno a příjmení.
- Vypiš jméno posledního kamaráda nebo kamarádky.
- Zjisti, zda má uživatel vyplněnou koresponednční adresu. Pokud ano, vypiš název města, kde uživatel žije.

Vytvoř soubor CSV, který obsahuje následující data:

- jméno,
- příjmení,
- rok narození,
- počet přátel,
- město, kde je možné jej zastihnout (korespondenční adresa, pokud je zadána, jinak trvalé bydliště).

Dále vytvoř seznam lidí, které můžeme zastihnout ve Středočeském kraji (PSČ začíná číslem 2)

# Maturita

```
Jméno,Český jazyk,Anglický jazyk,Matematika,Biologie,Chemie,Informatika
Guido van Rossum,1,1,1,1,1,
James Gosling,3,1,3,2,5,
Mads Torgersen,1,1,1,3,,1
```

Uvažuj program, který bude pracovat s výsledky z maturitní zkoušky. Data jsou v souboru [maturita.csv](maturita.csv). Každý maturoval povinně z českého jazyka, anglického jazyka, matematiky a biologie a dále si mohl vybrat mezi informatikou a chemií.

Student může mít jeden z následujících výsledků:

- "Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
- "Neprospěl", pokud má alespoň jednu pětku.
- "Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.

Nejprve vytvoř dvourozměrný seznam, kde na nulté pozici vnořeného seznamu bude jméno studenta a na první pozici jeho známky jako seznam čísel. Vynech prázdná políčka, tj. předměty, ze kterých student nematuroval. Dále vytvoř dvourozměrný seznam, kde na nulté pozici bude jméno studenta a na první pozici výsledek maturitní zkoušky (např. prospěl).

Následně výstup programu převeď na seznam slovníků. Seznam slovníků by měl vypadat jako na příkladu níže. Data zapiš do souboru ve formátu JSON.

```
[
    {
        "Jméno": "Guido van Rossum",
        "Výsledek": "Prospěl s vyznamenáním"
    },
    {
        "Jméno": "James Gosling",
        "Výsledek": "Neprospěl"
    },
    {
        "Jméno": "Mads Torgersen",
        "Výsledek": "Prospěl"
    }
]
```

# Soubor TSV

Načti soubor `battles.tsv` a vytvoř:

- Statistiku, kolikrát byl který rod v pozici útočníků. Útočníci jsou ve sloupcích `attacker_1` až `attacker_4`. Který rod je nejvíce útočný?
- Pokud je zadaná síla obou armád (sloupce `attacker_size` a `defender_size`, indexy sloupců jsou 17 a 18), vytvoř seznam bitev, kde slabší armáda zvítězila nad silnější (vítěze poznáš podle sloupce `attacker_outcome`, sloupec má index 13 a obsahuje hodnoty *win* a *loss*, do seznamu vlož název bitvy ze sloupce `name`, sloupec má index 0). Kolik takových bitev je?


# Bonus - Populace v USA

Použij API amerického statistického úřadu k získání dat o velikosti populace USA. Využij adresu `https://datausa.io/api/data?drilldowns=Nation&measures=Population`. Na dotaz API vrátí následující výstup:

```
{
   "data":[
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2020,
         "Year":"2020",
         "Population":326569308,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2019,
         "Year":"2019",
         "Population":324697795,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2018,
         "Year":"2018",
         "Population":322903030,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2017,
         "Year":"2017",
         "Population":321004407,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2016,
         "Year":"2016",
         "Population":318558162,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2015,
         "Year":"2015",
         "Population":316515021,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2014,
         "Year":"2014",
         "Population":314107084,
         "Slug Nation":"united-states"
      },
      {
         "ID Nation":"01000US",
         "Nation":"United States",
         "ID Year":2013,
         "Year":"2013",
         "Population":311536594,
         "Slug Nation":"united-states"
      }
   ],
   "source":[
      {
         "measures":[
            "Population"
         ],
         "annotations":{
            "source_name":"Census Bureau",
            "source_description":"The American Community Survey (ACS) is conducted by the US Census and sent to a portion of the population every year.",
            "dataset_name":"ACS 5-year Estimate",
            "dataset_link":"http://www.census.gov/programs-surveys/acs/",
            "table_id":"B01003",
            "topic":"Diversity",
            "subtopic":"Demographics"
         },
         "name":"acs_yg_total_population_5",
         "substitutions":[
            
         ]
      }
   ]
}
```

Ulož data jako soubor JSON. Soubor bude obsahovat slovník se dvojicemi "rok: velikost populace".

```
{
    "2020": 326569308,
    "2019": 324697795,
    "2018": 322903030,
    "2017": 321004407,
    "2016": 318558162,
    "2015": 316515021,
    "2014": 314107084,
    "2013": 311536594
}
```
