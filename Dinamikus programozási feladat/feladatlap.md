#### 3. Feladat: Dinamikus programozási feladat
#### Feladatleírás: Érmeváltás

[Link](https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=true)

Adott egy összeg és az elérhető pénzérme címletek, határozd meg, hányféleképpen lehet az adott összeget visszajáróként kiadni. Minden pénzérme típusból korlátlan mennyiség áll rendelkezésre.

**Példa**

_n_ = 3
_c_ = [8, 3, 1, 2]

Háromféleképpen lehet visszajárót adni _n_ = 3 esetén: {1, 1, 1}, {1, 2}, és {3}.

**Függvény leírása**

Egészítsd ki a _getWays_ függvényt.

A getWays függvény a következő paraméterekkel rendelkezik:

- int n: az összeg, amire visszajárót kell adni

- int c[m]: az elérhető érme címletek

**Visszatérés**

- int: a visszajáró adásának módjainak száma

**Bemenet formátuma**

Az első sor két szóközzel elválasztott egész számot tartalmaz, **_n_** és **_m_** értékeket, ahol:
**_n_** az összeg, amire visszajárót kell adni
**_m_** az érme típusok száma
A második sor **_m_** szóközzel elválasztott egész számokat tartalmaz, amelyek az egyes érme típusok értékeit írják le.

**Korlátozások**

- 1 <= c[i] <= 50
- 1 <= n <= 250
- 1 <= m <= 50
- Minden címlet _c[i]_ garantáltan különböző.

**Tippek**

Oldd meg az átfedő részfeladatokat dinamikus programozás (DP) használatával:
Ez a probléma rekurzívan is megoldható, de nem fog minden teszteseten átmenni anélkül, hogy optimalizálnád az átfedő részfeladatok kiküszöbölésére. Gondolkodj el azon, hogyan tárolhatod és hivatkozhatsz korábban kiszámított megoldásokra, hogy elkerüld ugyanazon részfeladat többszöri megoldását. * Vedd figyelembe a degenerált eseteket:

Hányféleképpen lehet **0** cent visszajárót adni?
Hányféleképpen lehet több mint **0** cent visszajárót adni, ha nincs érméd? * Ha nehézségeid vannak a megoldások tárolásának meghatározásában, akkor gondolkodj az alap eset szempontjából **(n = 0)**. - A válasz nagyobb lehet, mint egy **32** bites egész szám.

**Mintabemenet 0**
```
4 3
1 2 3
```
**Mintakimenet 0**
```
4
```
**Magyarázat 0**

Négyféleképpen lehet visszajárót adni **_n_ = 4** esetén a **C = [1, 2, 3]** értékű érmékkel:

1. {1, 1, 1, 1}
2. {1, 1, 2}
3. {2, 2}
4. {1, 3}

**Mintabemenet 1**
```
10 4
2 5 3 6
```
**Mintakimenet 1**
```
5
```
**Magyarázat 1**

Ötféleképpen lehet visszajárót adni **_n_ = 10** egységre a **C = [2, 5, 3, 6]** értékű érmékkel:

{2, 2, 2, 2, 2}
{2, 2, 3, 3}
{2, 2, 6}
{2, 3, 5}
{5, 5}