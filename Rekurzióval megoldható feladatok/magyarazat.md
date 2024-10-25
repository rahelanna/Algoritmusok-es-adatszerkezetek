#### Megoldás magyarázata
#### 2. Feladat: Rekurzióval megoldható feladatok

A feladatban adott egy egész szám, **_X_**, amelyet az **_N_**-edik hatványok egyedi természetes számokból álló 
összegével kell kifejezni. A cél az, hogy megtaláljuk, hányféleképpen lehet ezt megtenni.

Például ha **_X_ = 13** és **_N_ = 2**, akkor olyan egyedi természetes számokat keresünk, amelyek négyzetének 
összege **13**. Az egyetlen megoldás ebben az esetben:

**2^2 + 3^2 = 13**

A kimenet ennek megfelelően **1** lesz.

**Megoldási stratégia**

A probléma megoldása rekurzióval történik, amelynek során megpróbáljuk az összes lehetséges természetes számot 
felhasználni az **_N_**-edik hatványuk összegének képzéséhez. Ha sikeresen ki tudjuk fejezni **_X_**-et, akkor 
egy megoldást találtunk.

A megoldás rekurzív lesz, mivel egy adott szám hatványának felhasználása után megvizsgáljuk, hogy az adott szám 
levonása után a maradék érték újabb hatványokkal kifejezhető-e.

**Lépések a megoldáshoz**

**1. Rekurzív függvény megírása**

A _powerSum_ függvény egy rekurzív függvény segítségével próbálja meg kifejezni az **_X_** értéket az **_N_**-edik 
hatványok összegeként. 
A rekurzió során két ágat vizsgálunk meg:

- Az első ágon megpróbáljuk a számot levonni **_X_**-ből, és a maradékot újra vizsgáljuk.
- A második ágon figyelmen kívül hagyjuk az aktuális számot, és a következő számra lépünk.

**2. Rekurzió leállási feltételei:**

- Ha egy szám hatványa nagyobb, mint **_X_**, akkor abbahagyjuk az aktuális ágat, mivel ez az ág nem ad érvényes megoldást (visszatérünk **0**-val).
- Ha egy szám hatványa pontosan egyenlő **_X_**-szel, akkor egy érvényes megoldást találtunk (visszatérünk **1**-gyel).
- Egyébként a rekurziót folytatjuk, és mindkét ágat megvizsgáljuk (az aktuális szám használatával és anélkül).
    - Levonjuk a szám hatványát **_X_**-ből, és folytatjuk a maradékkal.
    - Nem vesszük figyelembe ezt a számot, és a következő számra lépünk.

**3. Rekurzió indítása:**

A rekurziót az **1**-es számmal indítjuk, mivel a legkisebb természetes szám, amelynek hatványát 
használhatjuk, az **1**.