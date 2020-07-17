title: Statistics: Exercises and Solutions
next_title: Statistics
next_url: %url:statistics%

## Correlating activity in the left and right brain


### Exercise

%-- include: exercises/numerical/statistics-2.md --%


### Solution

```python
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress
from scipy.signal import detrend

a = np.load('data/fmri-data.npy')
# Get the average over the left and right brain across all dimensions
# except time
left = a[:34].mean(axis=(0, 1, 2))
right= a[34:].mean(axis=(0, 1, 2))
# Detrend the signals and get the correlation between them
detrended_left = detrend(left)
detrended_right = detrend(right)
slope, intercept, r, p, se = linregress(detrended_left, detrended_right)
print('r = {:.4f}'.format(r))
# Create a nice plot!
xdata = np.arange(0, 90, 10)
plt.subplots_adjust(hspace=.4)
plt.subplot(2, 1, 1)
plt.plot(left, label='Left')
plt.plot(right, label='Right')
plt.xticks(xdata, 2 * xdata)
plt.xlabel('Time')
plt.xlim(0, 90)
plt.ylabel('BOLD')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(detrended_left)
plt.plot(detrended_right)
plt.xticks(xdata, 2 * xdata)
plt.xlabel('Time')
plt.xlim(0, 90)
plt.ylabel('BOLD')
plt.show()
```
