title: NumPy: Exercises and Solutions
next_title: numpy
next_url: %url:numpy%


## Activity in the left vs right brain

### Exercise

%-- include: exercises/numerical/numpy-2.md --%


### Solution

```python
import numpy as np

a = np.load('data/fmri-data.npy')
print(a.shape)
m_left = a[:34].mean()
m_right= a[34:].mean()
print('M(left) = {:.2f}'.format(m_left))
print('M(right) = {:.2f}'.format(m_right))
```
