title: DataMatrix: Exercises and Solutions
next_title: DataMatrix
next_url: %url:datamatrix%


```python
from datamatrix import io
from datamatrix import operations as ops
from datamatrix import series as srs

dm = io.readtxt('data/zhou_et_al_2020_exp1.csv')
sm = ops.group(dm, dm.subject_nr)
sm.mean_rt = srs.reduce_(sm.search_rt)
sm = ops.keep_only(sm, sm.subject_nr, sm.mean_rt)
lower = sm.mean_rt.mean - 2 * sm.mean_rt.std
upper = sm.mean_rt.mean + 2 * sm.mean_rt.std
outliers = (sm.mean_rt < lower) | (sm.mean_rt > upper)
for subject_nr in outliers.subject_nr:
    print('Removing subject {}'.format(subject_nr))
    dm = dm.subject_nr != subject_nr
```
