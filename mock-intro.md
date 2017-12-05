# Instalacja

Pod Pythonem 3.3+, nie wymaga instalowania dodatkowych paczek:

```python
from unittest import mock
```

Pod Pythonem 2.7 i 3.x, wymaga instalacji `pip install mock`:

```python
import mock
```

Wersja najbardziej uniwersalna:

```python
try:
    from unittest import mock
except ImportError:
    import mock
```

# Mocki imitujące funkcje

```python
>>> m = mock.Mock()  # konfiguracja mocka (na początku testu)
>>> m(42, foo=3)  # testowany kod wywołuje mocka zamiast prawdziwej funkcji
```

Pod koniec testu możemy sprawdzić, co się działo z mockiem:

```python
>>> m.assert_called_once_with()
>>> m.call_args
m(42, foo=3)
>>> m.call_args == mock.call(2, 4)
True
```

## Zwracanie wartości (`return_value`)

```python
>>> m = mock.Mock()
>>> m.return_value = 'foo'
>>> m()
'foo'
```

Mocka można skonfigurować od razu przy jego tworzeniu.
Poniższy kod jest równoważny wcześniejszemu:

```python
>>> m = mock.Mock(return_value='foo')
>>> m()
'foo'
```

## Rzucanie wyjątku (`side_effect`)

```python
>>> m = mock.Mock(side_effect=KeyError)
>>> m()
Traceback (most recent call last):
  ...
KeyError
```

## Zwracanie różnych wartości przy kolejnych wywołaniach

```python
>>> m = mock.Mock()
>>> m.side_effect = [
...     '1',
...     '2',
...     KeyError,
...     '3',
... ]
>>> m()
'1'
>>> m()
'2'
>>> m()
Traceback (most recent call last):
  ...
KeyError
>>> m()
'3'
```

## Delegowanie do własnej funkcji

```python
>>> m = mock.Mock()
>>> m.side_effect = lambda x: x+2
>>> m(5)
7
```

## Asercje funkcji-mocka

```python
m.assert_called_with(10)
m.assert_called_once_with(10)
m.assert_any_call(3)
m.assert_called_with(3)
m.assert_not_called()
```

## Inne użyteczne pola

```python
m.called
m.call_count
m.call_args  # argumenty ostatniego wywołania
m.call_args_list  # lista argumentów wszystkich wywołań
```

# Zagnieżdżanie mocków

```python
m = mock.Mock()
m.foo
m.foo.bar.egg.spam
m.foo.bar.egg.spam()
m.mock_calls
```
