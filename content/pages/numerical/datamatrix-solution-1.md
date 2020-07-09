title: DataMatrix: Exercises and Solutions
next_title: DataMatrix
next_url: %url:datamatrix%


```python
from datamatrix import io

dm = io.readxlsx('data/movies.xlsx')
dm = (dm.year > 1990) & (dm.year < 2000)
for year in dm.year.unique:
    year_dm = dm.year == year
    print('For movies from year {}, the mean rating is {:.2f}'.format(
        year,
        year_dm.rating.mean
    ))
```

An alternative solution makes use of `datamatrix.operations.split()`:

```python
from datamatrix import io, operations as ops

dm = io.readxlsx('data/movies.xlsx')
dm = (dm.year > 1990) & (dm.year < 2000)
for year, year_dm in ops.split(dm.year):
    print('For movies from year {}, the mean rating is {:.2f}'.format(
        year,
        year_dm.rating.mean
    ))
```
