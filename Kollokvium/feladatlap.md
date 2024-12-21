#### Kollokvium feladat
#### Feladatleírás: Játék a szavakkal
[Link](https://www.spoj.com/problems/WORDS1/)

Néhány titkos ajtó egy nagyon érdekes szójátékot tartalmaz. A régészek csapatának meg kell oldania ezt a rejtvényt, hogy kinyithassa az ajtókat. Mivel az ajtók kinyitásának nincs más módja, a rejtvény megoldása rendkívül fontos számunkra.

Minden ajtón számos mágneses lemez található. Minden lemezen egy szó van írva. A lemezeket olyan sorrendbe kell rendezni, hogy minden szó az előző szó utolsó betűjével kezdődjön. Például az "acm" szó után következhet a "motorola" szó. A feladatod egy számítógépes program megírása, amely a megadott szavak listáját beolvassa, és eldönti, hogy lehetséges-e a lemezeket egy sorrendbe állítani (a megadott szabály szerint), ezáltal kinyitva az ajtót.

**Bemenet**
A bemenet _T_ tesztesetből áll. Az első sorban a tesztesetek száma, _T_ (kb. 500), található. Minden teszteset egy sorral kezdődik, amely tartalmaz egy egész számot, N-et, amely a lemezek számát jelzi (_1 ≤ N ≤ 100000_). Ezután pontosan _N_ sor következik, amelyek mindegyike egy-egy szót tartalmaz. Minden szó legalább két és legfeljebb 1000 kisbetűs karakterből áll, vagyis csak az 'a'-tól 'z'-ig terjedő betűk jelenhetnek meg bennük. Ugyanaz a szó többször is megjelenhet a listában.

**Kimenet**
A programodnak meg kell állapítania, hogy lehetséges-e a lemezeket olyan sorrendbe állítani, hogy minden szó az előző szó utolsó betűjével kezdődjön. Az összes lemezt pontosan egyszer fel kell használni. Ha egy szó többször szerepel a listában, azt pontosan annyiszor kell felhasználni.

Ha létezik ilyen sorrend, a programnak az alábbi szöveget kell kiírnia: "**Ordering is possible**".  Egyébként ezt a szöveget írja ki: "**The door cannot be opened**".

**Példa**

```
Input

3
2
acm
ibm
3
acm
malfrom
mouse
2
ok
ok

Output

The door cannot be opened.
Ordering is possible.
The door cannot be opened.
```