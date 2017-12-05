# Behaviour Driven Development

**Behavior-Driven Development** to proces rozwoju oprogramowania bazujący na TDD w połączeniu z ideami zaczerpniętymi z Domain-Driven Design.

Metodologia BDD została opisana przez Dana Northa jako odpowiedź na szereg problemów, które napotykał w trakcie uczenia TDD. 

# Test akceptacyjny

BDD czerpie z metodologii Agile definiowanie wymagań przy pomocy „User Stories”. Wymagania zapisane przy pomocy „User Stories” są przekształcane do cech („features”) oraz scenariuszy i stają się wykonywalnym zestawem testów akceptacyjnych.

Upraszczając, test akceptacyjny to to samo co test funkcjonalny lub integracyjny.

BDD jest metodologią rozwoju oprogramowania, która kładzie nacisk na komunikację przy pomocy zwykłego języka. 
Dzięki temu w proces definiowania wymagań wraz z testami akceptacyjnymi mogą być zaangażowani klienci biznesowi.
Język użyty w procesie BDD jest językiem używanym przez klientów („Ubiquitous Language” z Domain-Driven Design).

W Pythonie użyjemy języka `Gherkin` i biblioteki `behave`.

# Test jednostkowy

Test jednostkowy to test pojedynczego modułu, klasy lub funkcji.

# Algorytm BDD

BDD składa się z dwóch zagnieżdżonych cykli.
Zewnętrzny cykl polega na napisaniu i zaliczeniu jednego testu akceptacyjnego.
W ramach tego cyklu pojawi się wiele cykli TDD.

1. Napisz najprostszy nieprzechodzący test akceptacyjny.
2. Dla każdego modułu, zaczynając od najwyższego:
    1. Dopóki nie zaimplementowano całego modułu, powtarzaj cykle TDD:
        1. Napisz najprostszy nieprzechodzący test jednostkowy.
        2. Napisz najprostszą implementację zaliczającą wszystkie testy.
        3. Zrefaktoryzuj testy i implementację.
3. Na tym etapie test akceptacyjny powinien zostać zaliczony.
    