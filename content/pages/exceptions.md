title: Exceptions


[TOC]



## `SyntaxError`s v `Exception`s

A `SyntaxError` occurs when you try to run syntactically invalid Python code. When this happens, the code is not executed at all, not even those lines that are syntactically valid. This is very different from an `Exception`!


```python
if x = 0: # = should be ==
    print('x is 0')
```

An `Exception` occurs when an error occurs during execution of syntactically valid Python code. In Python terminology, an `Exception` is *raised*.

Let's define an unsafe function.


```python
def oneover(i):

    return 1/i

```

If we call `oneover(0)`, we will get an `Exception`, more specially a `ZeroDivisionError`, because dividing any number by `0` is not allowed:

```python
oneover(0)
```

## Handling `Exception`s

### try … except …

Now let's use a `try … except …` statement to safely catch `Exception`s.

```python
try:
    i = oneover(0)
except: # A blank except is not preferred!
    print('Some problem occurred')
```

In the example above, if any `Exception` occurs in the block that follows the `try` statement, then the execution of that block is terminated, and the `except` block is executed.

It is good practice to specify which `Exception`s should be caught specifically. For example, `oneover()` can trigger a `ZeroDivisionError` error when we call it with `0` and a `TypeError` when we call it with a `str` or some other value that doesn't work in a numeric division. Therefore, we can specify that we want to catch only those two `Exception`s, and in addition specify that we want to keep the `Exception` object as the variable `e`.


```python
try:
    i = oneover(0)
except (TypeError, ZeroDivisionError) as e:
    print('A problem occurred: %s' % e)
```



### Re-raising (from)

We can also pass the `Exception` on after catching it, by doing a blank `raise`. Or a `raise … from` (only in Python 3).


```python
try:
    i = oneover(0)
except ZeroDivisionError as e:
    raise ValueError('Cannot divide by zero') from e

```

### else … finally

There is also an `else` block! This is executed when *no* `Exception` occurred during the `try` block. And finally there is also a `finally` block! This is always executed, and can be used to perform clean-up operations etc.


```python
try:
    i = oneover('x')
except ZeroDivisionError as e:
    print('Cannot divide by zero')
else:
    print('No exception occurred')
finally:
    print('This is always executed')
```

## Raising `Exception`s

You can raise `Exception`s yourself to indicate that something went wrong. It is good practice to use Python's built-in `Exception` objects whenever this makes sense.

```python
def factorial(n):

    if n < 0:
        raise ValueError('Factorial expects non-negative integers')
    return 1 if n == 0 else n*factorial(n-1)


factorial(-1)
```


But you can also create custom `Exception` objects.


```python
class FactorialError(Exception): pass


def factorial(n):

    if n < 0:
        raise FactorialError('Factorial expects non-negative integers')
    return 1 if n == 0 else n*factorial(n-1)


factorial(-1)
```
