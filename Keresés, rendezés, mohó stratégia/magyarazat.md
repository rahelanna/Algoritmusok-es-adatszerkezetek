#### Megoldás magyarázata
#### 1. Feladat: Keresés, rendezés, mohó stratégia

A feladat megoldása során Lauren célja, hogy minimális pénzügyi veszteséget szenvedjen el egy ház megvásárlásakor és 
eladásakor, két különböző évben. A feladat lényege, hogy az árakat tartalmazó listában megtaláljuk azt a két évet,
amelyekben a veszteség a lehető legkisebb, miközben biztosítjuk, hogy a vásárlás évének ára (price[i]) magasabb legyen, 
mint az eladás évének ára (price[j]).

A megoldási stratégia több lépésből áll, és ezek következetes megvalósítása vezet el a minimális veszteséghez.

**A szükséges adatok előkészítése**

A bemenet egy árlistából áll, amely tartalmazza az évekhez tartozó árakat. A cél, hogy olyan két árértéket találjunk, 
amelyek közötti különbség (veszteség) a lehető legkisebb. Ezenkívül fontos, hogy a vásárlás előbb történjen, mint az 
eladás, tehát az eredeti árlista sorrendje számít.

**Árindexek tárolása**

Ahhoz, hogy ellenőrizhessük, a vásárlási ár (price[i]) ténylegesen korábbi évben van, mint az eladási ár (price[j]), 
létrehozunk egy szótárt, amely tárolja minden ár eredeti indexét. Ez lehetővé teszi számunkra, hogy bármely két ár 
esetében gyorsan ellenőrizzük, hogy a vásárlás ténylegesen egy korábbi évben történt-e, mint az eladás.

**Mohó stratégia alkalmazása**

A feladat egyértelmű megoldása a mohó algoritmusok alkalmazásán alapul. Mohó stratégiával azt célozzuk, hogy minden 
egyes lépésben egy "helyes" választást hozzunk, amely a veszteséget csökkenti. Ez esetben ez azt jelenti, hogy először 
az árakat sorba rendezzük csökkenő sorrendben, hogy a legnagyobb veszteségeket kiszűrjük, majd megvizsgáljuk, hogy az 
eredeti árlistában a nagyobb ár tényleg megelőzi-e a kisebbet. Ha igen, akkor a veszteség érvényes.

**Iteráció**

Sorbarendezés után iterálunk az árak listáján, és minden lépésben kiszámítjuk az aktuális veszteséget 
(az előző és a következő ár különbségeként). Csak akkor vesszük figyelembe ezt a veszteséget, ha az eredeti árlistában 
a magasabb ár megelőzi az alacsonyabb árat, tehát a vásárlás előbb történt. Frissítjük a minimális veszteség értékét, 
ha az aktuális veszteség kisebb, mint az eddigi legkisebb veszteség.