title: Plotting: Exercises and Solutions
next_title: Plotting
next_url: %url:plotting%

## Plotting heart-rate distributions in subplots

### Exercise

%-- include: exercises/numerical/plotting-2.md --%


### Solution


```python
from matplotlib import pyplot as plt
import seaborn as sns
from datamatrix import io, operations as ops

dm = io.readtxt('data/heartrate.csv')
plt.subplot(2, 2, 1)
plt.subplots_adjust(wspace=.4, hspace=.8)
plt.title('Female Runners')
dm_female_runner = (dm.Gender == 'Female') & (dm.Group == 'Runners')
sns.distplot(dm_female_runner['Heart Rate'])
plt.subplot(2, 2, 2)
plt.title('Female Control')
dm_female_control = (dm.Gender == 'Female') & (dm.Group == 'Control')
sns.distplot(dm_female_control['Heart Rate'])
plt.subplot(2, 2, 3)
plt.title('Male Runners')
dm_male_runner = (dm.Gender == 'Male') & (dm.Group == 'Runners')
sns.distplot(dm_male_runner['Heart Rate'])
plt.subplot(2, 2, 4)
plt.title('Male Control')
dm_male_control = (dm.Gender == 'Male') & (dm.Group == 'Control')
sns.distplot(dm_male_control['Heart Rate'])
plt.show()
```
