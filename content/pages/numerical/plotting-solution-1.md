title: Plotting: Exercises and Solutions
next_title: Plotting
next_url: %url:plotting%


```python
from matplotlib import pyplot as plt
from datamatrix import io, operations as ops

dm = io.readxlsx('data/movies.xlsx')
dm = (dm.year >= 1990) & (dm.year < 2000)
for year, year_dm in ops.split(dm.year):
    plt.plot(sorted(year_dm.rating), label=year)
plt.legend(title='Year')
plt.ylabel('Rating')
plt.xlabel('Movie #')
plt.show()
```
