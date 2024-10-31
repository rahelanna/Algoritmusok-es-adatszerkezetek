#### 4. Feladat: Fák, gráfok
#### Feladatleírás: Utazás a Holdra

[Link](https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true)

Az ENSZ tagállamai azt tervezik, hogy két embert küldenek a Holdra. Azt szeretnék, ha különböző országokból érkeznének. Egy olyan listát kapsz, amely párokba rendezett űrhajós azonosítókból áll. Minden pár ugyanannak az országnak az űrhajósait tartalmazza. Határozd meg, hány olyan párt választhatnak ki, amely különböző országok űrhajósaiból áll.

**Példa**

**_n_ = 4** 
**_astronaut_ = [1, 2], [2, 3]**

Négy űrhajós van, akiket **0**-tól **3**-ig számoztak. Az országonként csoportosított űrhajósok: **[0]** és **[1, 2, 3]**. Három párosítás közül lehet választani: **[0, 1], [0, 2]** és **[0, 3]**.

**Függvény leírása**

Egészítsd ki a _journeyToMoon_ függvényt a szerkesztőben.

A _journeyToMoon_ függvény következő paraméterekkel rendelkezik:

- int n: az űrhajósok száma
- int astronaut[p][2]: minden **_astronaut[i]_** egy **2** elemű tömb, amely két azonosítóval jelzi ugyanazon ország űrhajósait

**Visszatérési érték**

- int: az érvényes párok száma

**Bemenet formátuma**

Az első sor két egész számot tartalmaz, **_n_** és **_p_**, amelyek az űrhajósok és a párok számát jelzik. A következő **_p_** sor mindegyike **2** szóközzel elválasztott egész számot tartalmaz, amelyek két azonos nemzetiségű űrhajós azonosítóit jelölik.

**Korlátozások**

- 1 <= n <= 10^5 
- 1 <= p <= 10^4

**Minta bemenet 0**
```
5 3 
0 1 
2 3 
0 4
```
**Minta kimenet 0**
```
6
```
**Magyarázat 0**

A **[0, 1, 4]** számmal jelölt személyek egy országhoz tartoznak, míg a **[2, 3]** számmal jelöltek egy másikhoz. Az ENSZ-nek **6** különböző módja van egy pár kiválasztására:

**[0, 2], [0, 3], [1, 2], [1, 3], [4, 2], [4, 3]**

**Minta bemenet 1**
```
4 1 
0 2
```
**Minta kimenet 1**
```
5
```
**Magyarázat 1**

A **[0, 2]** számmal jelölt személyek egy országhoz tartoznak, de az **1**-es és **3**-as személyek nem osztoznak másokkal országon. Az ENSZ-nek **5** különböző módja van egy pár kiválasztására:

**[0, 1], [0, 3], [1, 2], [1, 3], [2, 3]**
