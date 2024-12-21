#### Megoldás magyarázata
#### Kollokvium feladat, Játék a szavakkal

**Gráf építése**

A graph defaultdict segítségével kapcsolatot hozunk létre az szavak kezdő és záró karakterei között.
A gráf csúcsait az in_degree és out_degree tartja nyilván.
A szavak kapcsolatai határozzák meg a gráf irányított éleit.

**Euler-út feltételeinek ellenőrzése**
A csúcsok fokszámait ellenőrizve állapítjuk meg, hogy lehetséges-e az út.
A kód kiszámítja az összes csúcs fokkülönbségét és figyeli, hogy teljesülnek-e a feltételek:
- Amennyiben több mint 1 kezdő-, vagy végpont van, a sorrend nem lehetséges.
- Amennyiben bármelyik csúcs abszolút fokkülönbsége nagyobb, mint 1 a sorrend nem lehetséges.

Az Euler-út feltételei mellett a gráfnak összefüggőnek kell lennie a nem nullás fokú csúcsokat tekintve.
A kód mélységi keresést végez (DFS), hogy ellenőrizze, hogy az összes csúcs, amely része a gráfnak elérhető-e.

**Kimenet**

Ha az Euler-út feltételei teljesülnek és a gráf összefüggő:
```
Ordering is possible.
```

Egyébként:
```
The door cannot be opened.
```
