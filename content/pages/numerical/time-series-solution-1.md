title: Time series: Exercises and Solutions
next_title: Time series
next_url: %url:time-series%

## The impact of crises


### Exercise

%-- include: exercises/numerical/time-series-1.md --%


### Solution

First, load the data and process it. These are the same steps as described in more detail in the chapter.

```python
from datamatrix import io, NAN, series as srs, operations as ops

dm = io.readtxt('data/eurostat-gdp.csv')
dm.gdp[dm.gdp != int] = NAN
sm = ops.group(dm, by=dm.country)
shift = sm.year[:, 0] - 2000
sm.year = srs.roll(sm.year, shift)
sm.gdp = srs.roll(sm.gdp, shift)
```

Next, solve the exercise!

```python
from matplotlib import pyplot as plt

sm.gdp_2009_2007 = sm.gdp[:, 9] - sm.gdp[:, 7]
sm.gdp_2020_2019 = sm.gdp[:, 20] - sm.gdp[:, 19]
plt.figure(figsize=(11, 11))
plt.axhline(0, color='black', linestyle=':')
plt.axvline(0, color='black', linestyle=':')
plt.plot(sm.gdp_2009_2007, sm.gdp_2020_2019, 'o')
plt.xlabel('Per-capita GDP 2009 - 2007 (€)')
plt.ylabel('Per-capita GDP 2020 - 2019 (€)')
plt.axvline(sm.gdp_2009_2007.mean, color='red')
plt.axhline(sm.gdp_2020_2019.mean, color='red')
plt.show()
```
