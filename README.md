# SOE-ProgAlap1-Beadando-Motorterkep-Homor

A program egy egyszerű kis "házi nyilvántartás", motorozással kapcsolatban. A programban felvehetsz túrákat, hogy merre jártál, addhatsz hozzá több motort is és kiválaszthatod, hogy melyikkel mentél, megtekintheted a helyeket, ahol már jártál és ahol még nem. A program Vas megye településeire van korlátozódva.

## A következő menü fogad elinditáskor:
```
-------------------
|       Menü      |
-------------------
1) Túra bevitel
2) Helyek
3) Motorok
0) Kilépés
```
## 1. Túra bevitel
Itt lehet új túrát bevinni. Ha több motor van tárolva, akkor megkérdezi, hogy melyiket szeretnéd kiválasztani. Miután ez megtörtént, a program kéri a helyet, ahonnan indult a túra, majd ezt követően a következő helyeket, amiket érintett. Ha nem szeretnék több helyet felvenni, a "nincs" szöveg beírva a program nem kér be további helyeket. Ezután kiírja, hogy hány km-t tettünk meg, mikor, mennyi üzemanyag fogyott, illetve a gumik állapotáról egy megkőzelitőleges státuszt %-ban megadva, majd ezt elmenti a "tours.txt"-be.

## 2. Helyek
```
-------------------
|      Helyek     |
-------------------
1) Bejárt helyek
2) Eddig még be nem járt helyek
0) Vissza
```
Itt megtekinthető a helyek, ahol már jártunk, illetve ahol még nem.

## 3. Motorok
```
-------------------
|      Motorok    |
-------------------
1) Motorok megtekintése
2) Új motor hozzáadása
3) Motor törlése
0) Vissza
```
Itt megtekinthető, hogy hány motor van tárolva (motorbikes.txt). Itt lehet hozzáadni új motort, illetve törölni is.
## 0. Kilépés
A program bezáródik.

## Fájlok
- settlements.txt -> Vas megye települései és a hozzá tartozó kordináta.
- places.txt -> Itt tárolódnak azok a települések, amiket már felvettünk egy túránál, ergo a bejárt települések.
- tours.txt -> A túrák eltárolva.
- data.json -> Az eltárolt motorok.