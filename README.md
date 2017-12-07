# py-tdd-2017-12-05

# NBP

```html
<h1>Home Page</h1>
<p>{msg}</p>
<form method="POST">
  <p>Date: <input type="text" name="date" /></p>
  <p>Currency
    <select name="currency">
      <option value="USD">dolar amerykanski USD</option>
      <option value="THB">bat (Tajlandia) THB</option>
      <option value="ISK">korona islandzka ISK</option>
    </select>
  </p>
  <p><input type="submit" value="Get exchange rate!"></p>
</form>
```

## Przykładowe dane

| data | waluta | oczekiwane wyjście |
|-|-|-|
2017/01/02 | USD | 1 USD = 4.2106 PLN
2017/01/01 | USD | No data for this day.
2017/01/02 | ISK | 100 ISK = 3.7076 PLN
invalid | USD | Invalid input.

## Hint

```python
import datetime
DATE_FORMAT = '%Y/%m/%d'
date_as_str = request.form['date']
date = datetime.datetime.strptime(date_as_str, DATE_FORMAT).date()
```

# [Notatnik na hackmd.io](https://hackmd.io/AwUwxgrAzAHA7ATgLQhANjUgLAE2MJAI2DhCQgQCZY0ooKZCg===)
