#### Megoldás magyarázata
#### 2. Feladat: Rekurzióval megoldható feladatok

**Faktoriális és Inverz Számítás:**

**_compute_factorials függvény:_** 

egy faktorialis listát hozunk létre, amely a számok faktoriálisait tartalmazza 0-tól
n-ig, valamint egy inverz listát, amely minden szám faktoriálisának inverzét tárolja. 
Az inverzeket a Fermat tételével számítjuk ki egyszerűsítve.

**Permutáció Számítása:**

A **_count_permutations_** függvény először kiszámolja az összes permutációt, majd végigmegy minden karakter 
gyakoriságán, és elvégzi az osztást az ismétlődő karakterek faktoriálisaival. Az osztás moduláris szorzással 
történik az inverz lista segítségével.

**Eredmény Kiírása:**

A kód végén a **_count_permutations(s)_** függvény meghívásával és az eredmény kiírásával kapjuk meg a megoldást.