# Zasada pojedynczej odpowiedzialności *(Single-Responsibility Principle)*

Każda klasa lub moduł powinien mieć tylko jeden powód do zmiany.

Przykład złamania tej zasady: klasa `Employee` implementująca logikę biznesową (`.calculate_pay()`) i mechanizm utrwalania danych (`.save()`).

# Zasada otwarte-zamknięte *(Open/Close Principle)*

Klasy powinny być otwarte na rozbudowę i zamknięte na modyfikacje.

Jeśli dysponujemy klasą o określonym zachowaniu, które działa prawidłowo, należy uniemożliwić wprowadzenie modyfikacji w jej działającym kodzie.
W przypadku konieczności rozbudowy kodu (dodania nowej funkcjonalności), należy stworzyć klasy pochodne, w których można nadpisać wybrane metody i dostosować ich działanie do bieżących potrzeb.
Choć nie można modyfikować kodu klasy (zasada zamknięte), to jednak jest ona otwarta na rozbudowę (zasada otwarte).

Przykład złamania tej zasady: `Client` wykorzystuje bezpośrednio klasę `Server`. 
Zamiast tego, `Client` powinien korzystać z dowolnej klasy implementującej interfejs `ServerInterface`. 
Z kolei `Server` implementuje `ServerInterface`.

# Zasada podstawiania Liskov *(Liskov Substitution Principle)* 

Musi istnieć możliwość podstawiania typów pochodnych w miejsce ich typów bazowych.

Przykład złamania tej zasady: klasa `Square` dziedzicząca po klasie `Rectangle` udostępniającej gettery i settery dla szerokości jak i wysokości (`getWidth()`, `getHeight()`, `setWidth()`, `setHeight()`).

Aby zasada LSP była zachowana:

- warunki wstępne nie mogą być być bardziej restrykcyjne w typach pochodnych
- warunki końcowe nie mogą być luźniejsze w typach pochodnych
- niezmienniki muszą zostać zachowane

# Zasada segregacji interfejsów *(Interface Segregation Principle)*

Klient nie powinien być zmuszany do zależności od metod, których nie używa.

Przykład złej hierarchii: 

```python
class InputStream():
    def read(self): pass

class InputOutputStream(InputStream):
    def read(self): pass
    def write(self): pass
```

Jeżeli ktoś potrzebuje jedynie strumienia wyjściowego i używa tylko metody `write()`, wówczas przy takiej hierarchi interfejsów musi zażądać `InputOutputStream`. 
Klient jest wówczas zmuszony do dostarczenia obiektu implementującego dodatkowe metody (`read()`), które nie są wykorzystywane.

Poprawna hierarchia:

```python
class InputStream():
    def read(self): pass

class OutputStream():
    def write(self): pass

class InputOutputStream(InputStream, OutputStream):
    def read(self): pass
    def write(self): pass
```

# Zasada odwracania zależności *(Dependency Inversion Principle)*

- Moduły wysokopoziomowe nie powinny zależeć od modułów niskopoziomowych. 
  Obie grupy modułów powinny zależeć od abstrakcji.
- Abstrakcje nie powinny zależeć od szczegółowych rozwiązań. 
  To szczegółowe rozwiązania powinny zależeć od abstrakcji.

Stosowaniu tej zasady polega na dodaniu między modułem wysokopoziomowym a niskopoziomowym dodatkowej warstwy (fasady) z adapterami.