#### 1. Feladat: Keresés, rendezés, mohó stratégia
#### Feladatleírás: Minimális veszteség

[Link](https://www.hackerrank.com/challenges/minimum-loss/problem)

Lauren rendelkezik egy táblázattal, amely a következő néhány évre vonatkozóan mutatja egy ház különböző becsült árait. 
Egy évben meg kell vásárolnia a házat, és egy másik évben el kell adnia, és mindezt veszteséggel kell megtennie.
Azt szeretné, ha a pénzügyi vesztesége a lehető legkisebb lenne.

**Példa**

price = [20, 15, 8, 2, 12]

Minimális vesztesége abból adódik, hogy a 2. évben vásárol price[1] = 15 áron, 
és továbbértékesíti az 5. évben price[4] = 12 áron. Visszatérési érték: 15-12 = 3.

**Függvény leírása:**
Töltse ki a minimumLoss függvényt az alábbi szerkesztőben.

A minimumLoss paraméter a következővell rendelkezik:

- Int ár[n]: lakásárak minden évben

**Visszatér**

- int: A lehető legkisebb veszteség

**Bemeneti formátum**

Az első sor tartalmaz egy egész számot _n_, a házadatok éveinek számát.
A második sor _n_ szóközzel elválasztott hosszú egész számokat tartalmaz, 
amelyek leírják az egyes _price[i]_ tömb tagjait.

**Korlátok**

- 2 < = n <= 2 * 10^5
- 1 <= price[i] <= 10^16
- Minden ár eltérő.
- Van érvényes válasz.

**Altevékenységek**
- 2 <= _n_ <= 1000 a maximális pontszám 50%-ára.

**Minta bemenet 0**
```
3
5 10 3
```
**Minta kimenet 0**

```
2
```
**Magyarázat 0**

Lauren az **1.** évben megvásárolja a házat **_price_[0] = 5** áron, 
és eladja a **3.** évben **_price_[2]** minimális veszteségért, **5 - 3 = 2**.

**Minta bemenet 1**
```
5
20 7 8 2 5
```
**Minta kimenet 1**
```
2
```
**Magyarázat 1**

Lauren a **2.** évben megvásárolja a házat **_price_[1] = 7** áron, 
és eladja az **5.** évben **__price__[4]** áron minimális veszteségért, **7 - 5 = 2**.