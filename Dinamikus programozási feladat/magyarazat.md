#### Megoldás magyarázata
#### 3. Feladat: Dinamikus programozási feladat

A cél az, hogy meghatározzuk, hányféleképpen lehet összerakni egy adott összeget a rendelkezésre álló pénzérmékkel, 
ahol minden érmét korlátlanul használhatunk.

**Probléma megértése**

A feladat célja annak meghatározása, hogy hányféleképpen lehet egy adott **_n_** összeget megadott pénzérmékkel 
kifizetni. Az érmeértékek egy tömbben vannak megadva **(_c_)**, és minden egyes érme korlátlan számban áll rendelkezésre.

**Alapproblémák és megközelítés**

Ha **_n_ = 0**, azaz nincs pénzösszeg, amit vissza kell adni, akkor a megoldás **1** lesz, mivel egy üres lista is 
egy érvényes megoldásnak tekinthető.
Ha nincs érme, de az összeget vissza kellene adni, akkor nincs érvényes megoldás, tehát a megoldás **0** lesz.

Felosztjuk a problémát kisebb részproblémákra, és eltároljuk azok megoldásait, hogy ne kelljen többször megoldani 
ugyanazt a részproblémát.

**Megoldási lépések**

Létrehozunk egy **_dp_** táblát, ahol a **_dp[i]_** azt jelenti, hogy hányféleképpen lehet az _i_ összeget visszaadni.

Végigmegyünk minden érmecímleten:

Minden egyes érme esetében frissítjük a **_dp_** táblát az érme értékétől egészen **_n_**-ig minden összegre.
Minden összegnél hozzáadjuk a (összeg - érme) értékhez tartozó visszaadási módok számát az aktuális dp[összeg]-hez.

Végül visszaadjuk a **_dp[n]_** értéket, amely tartalmazza az **_n_** összeg visszaadásának összes lehetséges módját.