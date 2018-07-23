title: Loops: Exercises and Solutions
next_title: loops
next_url: %url:loops%


## Fibonacci

### Exercise

%-- include: exercises/basic/loops-1.md --%


### Solution

```python
prev = 1
curr = 1
print('0: {0}'.format(prev))
print('1: {0}'.format(curr))
i = 2
while True:
  prev, curr = curr, prev + curr
  if curr > 1000:
    break
  print('{0}: {1}'.format(i, curr))
  i += 1
```
