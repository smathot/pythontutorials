title: Statistics with SciPy and Statsmodels

[TOC]


## Libraries for statistics

[SciPy](https://www.scipy.org/) is a Python package with a large number of functions for numerical computing. It also contains statistical functions, but only for basic statistical tests (t-tests etc.). More advanced statistical tests are provided by [Statsmodels](https://www.statsmodels.org/stable/index.html). Statsmodels is powerful, but not very user-friendly; therefore, the tutorial below shows examples of several commonly used statistical tests.

All datasets used below are taken from the example data included with [JASP](https://jasp-stats.org/), with the exception of the [Zhou et al. (2020) dataset](https://doi.org/10.3758/s13414-020-02048-5) used for the Repeated Measures ANOVA.


## T-tests

### Independent-samples t-test

Consider a dataset from Matzke et al. (2015). In this dataset, participants performed a memory task in which they recalled a list of words. During the retention interval, one group of participants looked at a central fixation dot on a display. Another group of participants continuously made horizontal eye movements, which is believed by some to improve memory.

You can use the `ttest_ind()` function from `scipy.stats` to test whether memory performance (`CriticalRecall`) was higher for the horizontal-eye-movement group as compared to the fixation group. (There is a significant difference, but it goes in the opposite direction, such that the fixation group performed best.)


```python
from datamatrix import io
from scipy.stats import ttest_ind

dm = io.readtxt('data/matzke_et_al.csv')
dm_horizontal, dm_fixation = ops.split(dm.Condition, 'Horizontal', 'Fixation')
t, p = ttest_ind(dm_horizontal.CriticalRecall, dm_fixation.CriticalRecall)
print('t = {:.4f}, p = {:.4f}'.format(t, p))
```

It's always helpful to visualize the results:

```python
from matplotlib import pyplot as plt
import seaborn as sns

sns.barplot(x='Condition', y='CriticalRecall', data=dm)
plt.xlabel('Condition')
plt.ylabel('Memory performance')
plt.show()
```


### Paired-samples t-test

Consider a dataset from Moore, McCabe, & Craig. Here, aggressive behavior from people suffering from dementia was measured during full moon and another phase of the lunar cycle. Each participant was measured at both phases, i.e. this was a within-subject design.

You can use the `ttest_rel()` function to test whether aggression differed between the full moon and the other lunar phase. (Interestingly, it did.)


```python
from datamatrix import io
from scipy.stats import ttest_rel

dm = io.readtxt('data/moon-aggression.csv')
t, p = ttest_rel(dm.Moon, dm.Other)
print('t = {:.4f}, p = {:.4f}'.format(t, p))
```

And let's visualize the result. Because the measurements of the data are in two separate columns, we cannot easily use Seaborn for plotting. But we can resort to a quick plot with `plt.plot()`.

```python
from matplotlib import pyplot as plt

plt.plot([dm.Moon.mean, dm.Other.mean], 'o-')
plt.xticks([0, 1], ['Moon', 'Other'])
plt.ylabel('Aggression')
plt.xlabel('Lunar phase')
plt.show()
```

### One-sample t-test

If we take the difference between the Moon and Other measurements of the above dataset, then we can test this difference against zero (or another value specified with the `popmean` keyword) with `ttest_1samp()`:

```python
from datamatrix import io
from scipy.stats import ttest_1samp

dm = io.readtxt('data/moon-aggression.csv')
diff = dm.Moon - dm.Other
t, p = ttest_1samp(diff, popmean=0)
print('t = {:.4f}, p = {:.4f}'.format(t, p))
```

## Regression

### Correlation / simple linear regression

The following dataset, taken from Rotten Tomatoes, contains the 'freshness' rating and the Box Office profit for all of Adam Sandler's movies. You can use `linregress()` from `scipy.stats` to test if highly rated Adam Sandler movies make more money than poorly rated ones. (They don't.)

```python
from datamatrix import io
from scipy.stats import linregress

dm = io.readtxt('data/adam-sandler.csv')
slope, intercept, r, p, se = linregress(dm.Freshness, dm['Box Office ($M)'])
print('Box Office = {:.2f} * Freshness + {:.2f}'.format(slope, intercept))
print('p = {:.4f}, r = {:.4f}'.format(p, r))
```

To visualize this relationship, you can use Seaborn's `regplot()` function. Unfortunately, this function doesn't work with a DataMatrix object, and so we first need to convert this to a pandas DataFrame with the `to_pandas()` function from `datamatrix.convert`.


```python
from datamatrix import convert as cnv
from matplotlib import pyplot as plt
import seaborn as sns

df = cnv.to_pandas(dm)
sns.regplot(x='Freshness', y='Box Office ($M)', data=df)
plt.show()
```


### Multiple linear regression

Consider this dataset from Moore, McCabe, & Craig which contains grade-point averages (`gpa`) and SAT scores for mathematics (`satm`) and verbal knowledge (`satv`) for 500 high-school students. To test whether `satm` and `satv` are (uniquely) related to `gpa`, you can use the code below. (Only `satm` is uniquely related to `gpa`.)

The series of nested function calls (`ols(…).fit().summary()`) isn't very elegant, but the important part is the formula that is specified in a string with an R-style formula.

```python
from datamatrix import io
from statsmodels.formula.api import ols

dm = io.readtxt('data/gpa.csv')
print(ols('gpa ~ satm + satv', data=dm).fit().summary())
```


## ANOVA

### ANOVA (regular)

Let's go back to the heart-rate data from Moore, McCabe, and Craig. This dataset contains two factors that vary between subjects (Gender and Group) and one dependent variable (Heart Rate). To test whether Gender, Group, or their interaction affect heart rate, you need the following code. (They all do.)

As above, the combination of `ols()` and `anova_lm()` isn't very elegant, but the important part is the formula.

```python
from datamatrix import io
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

dm = io.readtxt('data/heartrate.csv')
dm.rename('Heart Rate', 'HeartRate')  # statsmodels doesn't like spaces
df = anova_lm(ols('HeartRate ~ Gender * Group', data=dm).fit())
print(df)
```

You can visualize this result with Seaborn:

```python
import seaborn as sns

sns.pointplot(x='Group', y='HeartRate', hue='Gender', data=dm)
plt.xlabel('Group')
plt.ylabel('Heart rate')
plt.show()
```

### Repeated Measures ANOVA

A Repeated Measures ANOVA is generally used to analyze data from experiments in which all participants take part in all conditions, that is, a within-subject design. An example of such a design comes from an experiment by [Zhou and colleagues](https://doi.org/10.3758/s13414-020-02048-5), in which participants searched for a target object in the presence of a distractor object. Either the target, or the distractor, or both could match a color that participants held in memory.

To test whether the factors distractor-match, target-match, and their interaction affect search accuracy, you can use the `AnovaRM` class from `statsmodels.stats.anova`. (They all do.)

Somewhat different most other RM-ANOVA software, the `AnovaRM` class accepts the data in long, unaggregated format. That is, each row corresponds to a single observation. Statsmodels will automatically reduce this format to a format where observations are aggregated per participant and condition (which is the required format for an RM-ANOVA) using the method indicated with the `aggregate_func` keyword:


```python
from pandas import pivot_table
from datamatrix import io, convert as cnv
from statsmodels.stats.anova import AnovaRM

dm = io.readtxt('data/zhou_et_al_2020_exp1.csv')
df = cnv.to_pandas(dm)
aov = AnovaRM(
    df,
    depvar='search_correct',
    subject='subject_nr',
    within=['target_match', 'distractor_match'],
    aggregate_func='mean'
).fit()
print(aov)
```

Let's visualize this result:

```python
import seaborn as sns

sns.pointplot(
    x='target_match',
    y='search_correct',
    hue='distractor_match',
    data=dm
)
plt.xlabel('Target match')
plt.ylabel('Search accuracy (proportion)')
plt.legend(title='Distractor match')
plt.show()
```

Tip: If you prefer to conduct the RM-ANOVA with different software, such as JASP or SPSS, then you first need to create a so-called pivot table, in which each row corresponds to a subject, and each column to a condition. You can do this with the `pandas.pivot_table()` function:

```python
from pandas import pivot_table
from datamatrix import io, convert as cnv

df = cnv.to_pandas(dm)
pm = pivot_table(
    df,
    values='search_correct',
    index='subject_nr',
    columns=['target_match', 'distractor_match']
)
print(pm)
```


## Exercises

<div class='info-box' markdown=1>

### A three-way Repeated Measures ANOVA

%-- include: exercises/numerical/statistics-1.md --%

[View solution](%url:statistics%-solution-1)

</div>
