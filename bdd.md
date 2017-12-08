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

Zewnętrzny cykl składa się z trzech kroków:

1. Napisanie najprostszego niezaliczonego testu akceptacyjnego.
2. Zaliczenie testu akceptacyjnego
3. Refaktoryzacja testów akceptacyjnych.

Drugi krok, czyli zaliczenie testu akceptacyjnego, polega na zastosowaniu TDD dla wszystkich modułów, zaczynając od najwyższego (podejście outside-in).
TDD jest tutaj wewnętrznym cyklem.

Dokładny algorytm wygląda następująco:

1. Napisz najprostszy nieprzechodzący test akceptacyjny.
2. Dla każdego modułu, zaczynając od najwyższego, wykorzystaj TDD:
    1. Jeśli rozpatrzyliśmy już wszystkie moduły, przejdź do dużego trzeciego kroku.
    2. Jeśli nie potrzebujemy więcej testów dla tego modułu, skocz do podkroku 1.
    3. Napisz najprostszy nieprzechodzący test jednostkowy.
    4. Napisz najprostszą implementację zaliczającą wszystkie testy.
    5. Zrefaktoryzuj testy i implementację.
    6. Skocz do podkroku 2.
3. Na tym etapie test akceptacyjny powinien zostać zaliczony (może być konieczne wprowadzenie drobnych zmian).
4. Refaktoring testów akceptacyjnych
5. Jeżeli potrzeba zaimplementować więcej funkcjonalności, skocz do kroku 1.
