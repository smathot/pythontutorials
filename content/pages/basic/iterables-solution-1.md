title: Iterables: Exercises and Solutions
next_title: Iterables
next_url: %url:iterables%


## Fibonacci

### Exercise

%-- include: exercises/basic/iterables-1.md --%


### Solution

```python
fibonacci = [1, 1, 2, 3, 5, 8]
even_fibonacci = fibonacci[::2]
odd_fibonacci = fibonacci[1::2]
print('Fibonacci at even positions: {0}'.format(even_fibonacci))
print('Fibonacci at odd positions: {0}'.format(odd_fibonacci))
```
