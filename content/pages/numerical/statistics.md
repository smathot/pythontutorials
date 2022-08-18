title: Statistics with SciPy, Statsmodels, and Pingouin
next_title: Time series
next_url: %url:time-series%

[TOC]


## Libraries for statistics


### SciPy

[SciPy](https://www.scipy.org/) is a Python package with a large number of functions for numerical computing. It also contains statistical functions, but only for basic statistical tests (t-tests etc.).


### Statsmodels

More advanced statistical tests are provided by [Statsmodels](https://www.statsmodels.org/stable/index.html). Statsmodels is powerful, but not very user-friendly; therefore, the tutorial below shows examples of several commonly used statistical tests.


### Pingouin

[Pingouin](https://pingouin-stats.org/) is a relatively new Python library for statistics. It provides more uniform and user-friendly functions than SciPy and Statsmodels.


## Example datasets

All datasets used below are taken from the example data included with [JASP](https://jasp-stats.org/), with the exception of the [Zhou et al. (2020) dataset](https://doi.org/10.3758/s13414-020-02048-5) used for the Repeated Measures ANOVA.


## T-tests

### Independent-samples t-test

Consider [this dataset](/data/matzke_et_al.csv) from Matzke et al. (2015). In this dataset, participants performed a memory task in which they recalled a list of words. During the retention interval, one group of participants looked at a central fixation dot on a display. Another group of participants continuously made horizontal eye movements, which is believed by some to improve memory.

You can use the `ttest_ind()` function from `scipy.stats` to test whether memory performance (`CriticalRecall`) was higher for the horizontal-eye-movement group as compared to the fixation group.


```python
from datamatrix import io, operations as ops
from scipy.stats import ttest_ind

dm = io.readtxt('data/matzke_et_al.csv')
dm_horizontal, dm_fixation = ops.split(dm.Condition, 'Horizontal', 'Fixation')
t, p = ttest_ind(dm_horizontal.CriticalRecall, dm_fixation.CriticalRecall)
print('t = {:.4f}, p = {:.4f}'.format(t, p))
```

This reveals a significant difference (*p* = .0066). However, as you can see in the figure below, the effect goes in the opposite direction from the prediction, such that the fixation group performed best.

You can also use the `ttest()` function from `pingouin`. This also provides a Bayes Factor, for those who are into Bayesian statistics.

```python
import pingouin as pg

df = pg.ttest(dm_horizontal.CriticalRecall, dm_fixation.CriticalRecall)
print(df)
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

Consider [this dataset](/data/moon-aggression.csv) from Moore, McCabe, & Craig. Here, aggressive behavior from people suffering from dementia was measured during full moon and another phase of the lunar cycle. Each participant was measured at both phases, i.e. this was a within-subject design.

You can use the `ttest_rel()` function to test whether aggression differed between the full moon and the other lunar phase.


```python
from datamatrix import io
from scipy.stats import ttest_rel

dm = io.readtxt('data/moon-aggression.csv')
t, p = ttest_rel(dm.Moon, dm.Other)
print('t = {:.4f}, p = {:.4f}'.format(t, p))
```

Interestingly, there was indeed a significant effect (*p* < .0001; note that *p* values are never 0 as the output implies!), and this effect was in such that people were indeed most aggressive during full moon, as you can see in the figure below.

You can also use the `ttest()` function from `pingouin` and use the `paired` keyword to indicate that this is a paired-samples t-test, as opposed to an independent-samples t-test.

```python
import pingouin as pg

df = pg.ttest(dm.Moon, dm.Other, paired=True)
print(df)
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

If we take the difference between the Moon and Other measurements of [the above dataset](/data/moon-aggression.csv), then we can test this difference against zero (or another value specified with the `popmean` keyword) with `ttest_1samp()`:

```python
from datamatrix import io
from scipy.stats import ttest_1samp

dm = io.readtxt('data/moon-aggression.csv')
diff = dm.Moon - dm.Other
t, p = ttest_1samp(diff, popmean=0)
print('t = {:.4f}, p = {:.4f}'.format(t, p))
```

You can also use the `ttest()` function from `pingouin`. To indicate that this is a one-sample t-test against zero, simply pass 0 as the second argument.

```python
import pingouin as pg

df = pg.ttest(diff, 0)
print(df)
```

## Regression

### Correlation / simple linear regression

[This dataset](/data/adam-sandler.csv), taken from Rotten Tomatoes, contains the 'freshness' rating and the Box Office profit for all of Adam Sandler's movies. You can use `linregress()` from `scipy.stats` to test if highly rated Adam Sandler movies make more money than poorly rated ones.

```python
from datamatrix import io
from scipy.stats import linregress

dm = io.readtxt('data/adam-sandler.csv')
slope, intercept, r, p, se = linregress(dm.Freshness, dm['Box Office ($M)'])
print('Box Office = {:.2f} * Freshness + {:.2f}'.format(slope, intercept))
print('p = {:.4f}, r = {:.4f}'.format(p, r))
```

There seems to be no notable relationship between the freshness ratings of Adam Sandler's movies and their Box Office profit (*p* = .8785), as you can also see in the figure below.

You can also use the `linear_regression()` function from `pingouin`. Here, the intercept and slope simply correspond to the first and second values in the `coef` column.

```python
import pingouin as pg

df = pg.linear_regression(X=dm.Freshness, y=dm['Box Office ($M)'])
print(df)
```

To get the correlation, you can use the `corr` function from `pingouin`.

```python
df = pg.corr(dm.Freshness, dm['Box Office ($M)'])
print(df)
```

To visualize this relationship, you can use Seaborn's `regplot()` function.


```python
from matplotlib import pyplot as plt
import seaborn as sns

sns.regplot(x='Freshness', y='Box Office ($M)', data=dm)
plt.show()
```


### Multiple linear regression

Consider [this dataset](/data/gpa.csv) from Moore, McCabe, & Craig which contains grade-point averages (`gpa`) and SAT scores for mathematics (`satm`) and verbal knowledge (`satv`) for 500 high-school students. To test whether `satm` and `satv` are (uniquely) related to `gpa`, you can use the code below.

The series of function calls (`model = ols(…).fit()` and then `model.summary()`) isn't very elegant, but the important part is the formula that is specified in a string with an R-style formula.

```python
from datamatrix import io
from statsmodels.formula.api import ols

dm = io.readtxt('data/gpa.csv')
model = ols('gpa ~ satm + satv', data=dm).fit()
print(model.summary())
```

This reveals that only SAT scores for mathematics (*t* = 3.444, *p* = .001), but not for verbal knowledge (*t* = -0.040, *p* = .968), are uniquely related to grade point average.

You can also use the `linear_regression()` function from `pingouin`. The first argument, `X`, now consists of multiple columns (as opposed to a single column when doing a simple linear regression). To select the columns that should be used as predictors, you can simply select them directly from the datamatrix (`dm['satm', 'satv']`).

```python
import pingouin as pg

df = pg.linear_regression(X=dm['satm', 'satv'], y=dm.gpa)
print(df)
```


## ANOVA

### ANOVA (regular)

Let's go back to [this heart-rate data](/data/heartrate.csv) from Moore, McCabe, and Craig. This dataset contains two factors that vary between subjects (Gender and Group) and one dependent variable (Heart Rate). To test whether Gender, Group, or their interaction affect heart rate, you need the following code.

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

This reveals that heart rate is related to all factors: gender (*F* = 185.980, *p* < .001), group (*F* = 695.647, *p* < .001), and the gender-by-group interaction (*F* = 7.409, *p* = .006).

You can also use the `anova` function from `pingouin`.

```python
import pingouin as pg

aov = pg.anova(dv='HeartRate', between=['Gender', 'Group'], data=dm)
print(aov)
```

You can visualize this result with Seaborn:

```python
from matplotlib import pyplot as plt
import seaborn as sns

sns.pointplot(x='Group', y='HeartRate', hue='Gender', data=dm)
plt.xlabel('Group')
plt.ylabel('Heart rate')
plt.show()
```

### Repeated Measures ANOVA

A Repeated Measures ANOVA is generally used to analyze data from experiments in which all participants take part in all conditions, that is, a within-subject design. An example of such a design comes from an experiment by [Zhou and colleagues](https://doi.org/10.3758/s13414-020-02048-5), in which participants searched for a target object in the presence of a distractor object. Either the target, or the distractor, or both could match a color that participants held in memory. You can download [this dataset here](/data/zhou_et_al_2020_exp1.csv).

To test whether the factors distractor-match, target-match, and their interaction affect search accuracy, you can use the `AnovaRM` class from `statsmodels.stats.anova`.

Somewhat different most other RM-ANOVA software, the `AnovaRM` class accepts the data in long, unaggregated format. That is, each row corresponds to a single observation. Statsmodels will automatically reduce this format to a format where observations are aggregated per participant and condition (which is the required format for an RM-ANOVA) using the method indicated with the `aggregate_func` keyword:


```python
from datamatrix import io
from statsmodels.stats.anova import AnovaRM

dm = io.readtxt('data/zhou_et_al_2020_exp1.csv')
aov = AnovaRM(
    dm,
    depvar='search_correct',
    subject='subject_nr',
    within=['target_match', 'distractor_match'],
    aggregate_func='mean'
).fit()
print(aov)
```

This reveals that search accuracy is affected by all factors: target match (*F* = 6.7339, p = .0139), distractor match (*F* = 13.9729, *p* = .0007), and the target match by distractor match interaction (*F* = 7.1687, *p* = .0113).

You can also use the `rm_anova` function from `pingouin`.


```python
import pingouin as pg

aov = pg.rm_anova(
    dv='search_correct',
    within=['target_match', 'distractor_match'],
    subject='subject_nr',
    data=dm
)
print(aov)
```

Let's visualize this result.

We could (but shouldn't!) simply create a `pointplot` based on `dm`. But this plot would not take into account that a Repeated Measures ANOVA is based on aggregated data (i.e. one observation per condition and participant). And therefore the error bars of this plot would not reflect the variation between participants (as it should), but rather the variation between individidual trials. 

To make a more appropriate figure, we first use `ops.group()` to create a new datamatrix, `gm`, in each row corresponds to a single condition for a single participant. Initially, `gm.search_correct` then corresponds to a series of values, one for each trial. (It is a `SeriesColumn`, a powerful type of column about which you can read more [here](https://pydatamatrix.eu/series-tutorial/).) We use `srs.reduce_()` to change this series of values to a single, mean value. Finally, we remove the between-subject variability, which is a fancy way of saying that we change `search_correct` such that it is on average the same for each participant, without changing the overall average of `search_correct` across participants. (This procedure is described in more detail in [this blogpost](https://www.cogsci.nl/blog/tutorials/156-an-easy-way-to-create-graphs-with-within-subject-error-bars).)

And then we can finally create a plot that is an appropriate match to the Repeated Measures ANOVA!


```python
from matplotlib import pyplot as plt
import seaborn as sns
from datamatrix import operations as ops, series as srs

# Group the data by condition and subject
gm = ops.group(
    dm,
    by=[dm.target_match, dm.distractor_match, dm.subject_nr]
)
gm.search_correct = srs.reduce_(gm.search_correct)
# Remove between-subject variability
for subject_nr, sm in ops.split(gm.subject_nr):
    gm.search_correct[sm] = sm.search_correct - sm.search_correct.mean + gm.search_correct.mean
# And plot!
sns.pointplot(
    x='target_match',
    y='search_correct',
    hue='distractor_match',
    data=gm
)
plt.xlabel('Target match')
plt.ylabel('Search accuracy (proportion)')
plt.legend(title='Distractor match')
plt.show()
```

Tip: If you prefer to conduct the RM-ANOVA with different software, such as JASP or SPSS, then you first need to create a so-called pivot table, in which each row corresponds to a subject, and each column to a condition. You can do this with the `ops.pivot_table()` function:

```python
pm = ops.pivot_table(
    dm,
    values=dm.search_correct,
    index=dm.subject_nr,
    columns=[dm.target_match, dm.distractor_match]
)
print(pm)
```


## Linear mixed-effects modeling

A linear mixed-effects model (or: linear mixed-effects regression) is a modern statstical-analysis technique for 'hierarchical' datasets. This sounds complicated, but the most common type of hierarchy is simply a dataset that consists of multiple observations from multiple participants. The Zhou et al. dataset, described [above](#repeated-measures-anova), is an example of such a dataset.

In many cases, you can analyze the same dataset using either a Repeated Measures ANOVA or a linear mixed-effects model; however, one crucial difference is that a Repeated Measures ANOVA requires you to aggregate data across multiple observations (e.g. by calculating the mean reaction time per participant and condition), whereas a linear mixed-effects model is performed on unaggregated data, i.e. on individual observations. In addition, linear mixed-effects modeling offers far more flexibility for analyzing complex datasets that you cannot analyze with a Repeated Measures ANOVA.

Let's say that we want to analyze search reaction times as a function of the conditions target match and distractor match, and that we want to have random by-participant intercepts and slopes. The most well-known package for linear mixed-effects modeling is the R package `lme4`, in which case this analysis corresponds to the formula:

```R
search_rt ~ target_match * distractor_match + (1 + target_match * distractor_match | subject_nr)
```

In Python, we need to use `statsmodels` for this, and the syntax is slightly different. Notably, the random effects structure is passed separately as the `re_formula` keyword:

```python
from datamatrix import io
from statsmodels.formula.api import mixedlm

dm = io.readtxt('data/zhou_et_al_2020_exp1.csv')
model = mixedlm(formula='search_rt ~ target_match * distractor_match',
                re_formula='~ target_match * distractor_match',
                data=dm, groups='subject_nr').fit()
print(model.summary())
```

This reveals that search reaction times are affected by all factors: target match (*z* = -6.579, *p* < .001), distractor match (*z* = 5.230, *p* < .001), and the target match by distractor match interaction (*z* = 2.492, *p* = .013).


## Exercises

<div class='info-box' markdown=1>

### A three-way Repeated Measures ANOVA

%-- include: exercises/numerical/statistics-1.md --%

[View solution](%url:statistics%-solution-1)

</div>

<div class='info-box' markdown=1>

### Correlating activity in the left and right brain

%-- include: exercises/numerical/statistics-2.md --%

[View solution](%url:statistics%-solution-2)

</div>
