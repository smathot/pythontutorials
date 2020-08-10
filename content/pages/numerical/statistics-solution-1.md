title: Statistics: Exercises and Solutions
next_title: Statistics
next_url: %url:statistics%


## A three-way Repeated Measures ANOVA


### Exercise

%-- include: exercises/numerical/statistics-1.md --%


### Solution

```python
from pandas import pivot_table
from datamatrix import io
from datamatrix import operations as ops
from statsmodels.stats.anova import AnovaRM
import seaborn as sns

# Read the data and pass it to AnovaRM
dm = io.readtxt('data/zhou_et_al_2020_exp1.csv')
aov = AnovaRM(
    dm,
    depvar='search_correct',
    subject='subject_nr',
    within=[
        'target_match',
        'distractor_match',
        'congruency'
    ],
    aggregate_func='mean'
).fit()
print(aov)
# Now plot the data!
dm_congruent, dm_incongruent = ops.split(dm.congruency, 1, 0)
plt.subplots_adjust(wspace=0.4)
plt.subplot(1, 2, 1)
plt.title('Congruent')
sns.pointplot(
    x='target_match',
    y='search_correct',
    hue='distractor_match',
    data=dm_congruent
)
plt.ylim(0.75, 1)
plt.xlabel('Target match')
plt.ylabel('Search accuracy (proportion)')
plt.legend(title='Distractor match')
plt.subplot(1, 2, 2)
plt.title('Incongruent')
sns.pointplot(
    x='target_match',
    y='search_correct',
    hue='distractor_match',
    data=dm_incongruent
)
plt.ylim(0.75, 1)
plt.xlabel('Target match')
plt.ylabel('Search accuracy (proportion)')
plt.legend(title='Distractor match')
plt.show()
```
