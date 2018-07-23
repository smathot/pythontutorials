title: Functions: Exercises and Solutions
next_title: Functions
next_url: %url:functions%


## Factorial using recursion

### Exercise

%-- include: exercises/basic/functions-2.md --%


### Solution

```python
def factorial(i):

  if not i: # 0 is False
    return 1
  return i * factorial(i - 1)


print('0! == {0}'.format(factorial(0)))
print('1! == {0}'.format(factorial(1)))
print('2! == {0}'.format(factorial(2)))
print('3! == {0}'.format(factorial(3)))
```
