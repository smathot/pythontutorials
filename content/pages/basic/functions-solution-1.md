title: Functions: Exercises and Solutions
next_title: Functions
next_url: %url:functions%


## Factorial using for

### Exercise

%-- include: exercises/basic/functions-1.md --%


### Solution

```python
def factorial(i):

  f = 1
  for j in range(i):
    f *= j + 1
  return f


print('0! == {0}'.format(factorial(0)))
print('1! == {0}'.format(factorial(1)))
print('2! == {0}'.format(factorial(2)))
print('3! == {0}'.format(factorial(3)))
```
