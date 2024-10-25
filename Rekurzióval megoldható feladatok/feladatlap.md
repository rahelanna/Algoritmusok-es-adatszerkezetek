#### 2. Feladat: Rekurzióval megoldható feladatok
#### Feladatleírás: Hatványösszeg

[Link](https://www.hackerrank.com/challenges/the-power-sum/problem)

Add meg, hogy egy adott egész szám, **_X_**, hányféleképpen fejezhető ki egyedi, természetes számok **_N_**-edik
hatványainak összegével.

Például, ha **_X_ = 13** és **_N_ = 2**, meg kell találnunk az összes olyan kombinációt, ahol egyedi négyzetek összege 
adja ki a **13**-at. Az egyetlen megoldás a **2^2 + 3^2**.

**Függvény leírása**

Töltsd ki a powerSum függvényt az alábbi szerkesztőben. A függvénynek egy egész számot kell visszaadnia, amely az 
összes lehetséges kombináció számát jelenti.

A powerSum függvény a következő paraméterekkel rendelkezik:

- X: az az egész szám, amelyre az összeget keressük 
- N: az az egész szám, amelyre a számokat hatványozzuk

**Bemeneti formátum**

Az első sor tartalmaz egy **_X_** egész számot. 
A második sor tartalmaz egy **_N_** egész számot.

**Korlátok**

- 1 <= X <= 1000 
- 2 <= N <= 10

**Kimeneti formátum**

Adjon vissza egyetlen egész számot, amely a kiszámított lehetséges kombinációk számát jelenti.

**Minta bemenet 0**
```
10 
2
```
**Minta kimenet 0**
```
1
```
**Magyarázat 0**

Ha **_X_ = 10** és **_N_ = 2**, meg kell találnunk, hogy hányféleképpen lehet a **10**-et egyedi négyzetek 
összegeként kifejezni.

**10 = 1^2 + 3^2**

Ez az egyetlen módja annak, hogy a **10**-et egyedi négyzetek összegeként fejezzük ki.

**Minta bemenet 1**
```
100 
2
```
**Minta kimenet 1**
```
3
```
**Magyarázat 1**

**100 = (10^2) = (6^2 + 8^2) = (1^2 + 3^2 + 4^2 + 5^2 + 7^2)**

**Minta bemenet 2**
```
100 
3
```
**Minta kimenet 2**
```
1
```
**Magyarázat 2**

A **100** kifejezhető az **1, 2, 3, 4** számok köbeinek összegeként. **(1 + 8 + 27 + 64 = 100)**. 
Nincs más mód arra, hogy a 100-at a köbök összegeként kifejezzük.