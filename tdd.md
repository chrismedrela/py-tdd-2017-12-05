# Algorytm TDD

Aplikacja TDD jest rozwijana w mikro-cyklach

1. **Red**: Napisz najprostszy test, który nie przechodzi
2. **Green**: Napisz minimalną ilość kodu zaliczającą ten test
3. **Refaktor**: Zrefaktoryzuj, zarówno testy jak i implementację

Ten cykl nazywa się cyklem Red-Green-Refactor.

# Trzy prawa TDD

1. Nie można zacząć pisać kodu produkcyjnego przed zakończeniem pisania testu jednostkowego, który nie jest spełniony.
2. Kod testu jednostkowego powinien być tylko tak długi, aby wystarczył do niespełnienia testu, a błędna kompilacja jest jednocześnie nieudanym testem.
3. Nie można pisać większej ilości kodu, niż jest wymagana do przejścia testu jednostkowego.

# Zalety TDD

- Testy jako dokumentacja
- Testy jako kryteria akceptacji
- Projektowanie interfejsu nakierowane na klienta
- Zestaw testów regresyjnych
- Unikamy overengineering'u
- Wyłapujemy błędy we wczesnej fazie projektu

# F.I.R.S.T.

Dobre testy jednostkowe powinny spełniać pięć zasad:

1. **Szybkie _(Fast)_** - Testy powinny wykonywać się szybko.
2. **Niezależne _(Independent)_** - Testy nie powinny zależeć od siebie.
3. **Powtarzalne _(Repeatable)_** - Testy powinny być powtarzalne w każdym środowisku.
4. **Samokontrolujące _(Self-Validating)_** - Testy powinny mieć jeden parametr wyjściowy typu logicznego. Mogą się powieść albo nie.
5. **O czasie _(Timely)_** - Testy powinny być pisane w odpowiednim momencie. Testy jednostkowe powinny być pisane bezpośrednio przed tworzeniem kodu produkcyjnego.