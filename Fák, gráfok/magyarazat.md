#### Megoldás magyarázata
#### 4. Feladat: Fák, gráfok

**Probléma áttekintése**

A feladatban meg kell számolni, hogy hányféleképpen választhatunk ki két különböző országból származó űrhajóst, ha adott egy lista, amely az ugyanazon országból származó űrhajós párokat tartalmazza.

**Megoldási stratégia**

Ez egy gráf probléma, és a gráf összefüggő komponenseinek tulajdonságaira épít. 

**Gráf modellezése**

Az űrhajósokat a gráf csomópontjaiként ábrázoljuk.
Az ugyanazon országból származó űrhajós párok élekkel vannak összekötve.
A gráf minden összefüggő komponense egy országot képvisel.

**Összefüggő komponensek megtalálása**

Mélységi keresést (DFS) alkalmazunk az összes összefüggő komponens azonosítására.
Minden DFS bejárás egy ország (összefüggő komponens) méretét adja meg.

**Párok számítása**

Ahelyett, hogy közvetlenül számolnánk a különböző országok közötti párokat, egy okos matematikai megközelítést alkalmazunk.
Kiszámítjuk az összes lehetséges pár számát, majd kivonjuk az ugyanazon országból származó párok számát.


Iteratív mélységi keresést (DFS) használunk, hogy elkerüljük a verem túlcsordulási problémáit nagy bemenetek esetén.
A függvény az összefüggő komponensek (országok) méretét adja vissza.
```
def iterative_dfs(start, visited):
    stack = [start]
    size = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            size += 1
            stack.extend(neighbor for neighbor in graph[node] if not visited[neighbor])
    return size
```

Végigiteráljuk az össze asztronautát:
```
visited = [False] * n
total_sum = 0
squared_sum = 0

for i in range(n):
    if not visited[i]:
        size = iterative_dfs(i, visited)
        total_sum += size
        squared_sum += size * size
```
Minden lehetséges pár számolása:
```
 total_pairs = (total_sum * (total_sum - 1) // 2) - (squared_sum - total_sum) // 2
```