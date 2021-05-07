title: Exceptions: error handling
next_title: NumPy
next_url: %url:numpy%


[TOC]



## `SyntaxError`s v `Exception`s

A `SyntaxError` occurs when you try to run syntactically invalid Python code, that is, when you're asking Python to execute code that is not actually Python code. When this happens, the code is not executed at all, not even those lines that are syntactically valid. This is very different from an `Exception`!


```python
# should-raise
if x = 0: # = should be ==
  print('x is 0')
```

An `Exception` occurs when there is an error during execution of syntactically valid Python code. In Python terminology, an `Exception` is *raised*. To illustrate this, let's define an unsafe function, that is, a function that can easily result in an `Exception`.


```python
def oneover(i):

  return 1/i
```

Calling `oneover(0)` results in a `ZeroDivisionError` (a special kind of `Exception`) because dividing any number by `0` is not allowed:

```python
# should-raise
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
print("I'm still alive!")
```

In the example above, if any `Exception` occurs in the block that follows the `try` statement, then the execution of that block is terminated, and the `except` block is executed. Importantly, however, the code continues to run.

It is good practice to specify *which* `Exception`s should be caught. For example, `oneover()` triggers a `ZeroDivisionError` error when called with `0` and a `TypeError` called it with a `str` or some other value that doesn't work in a numeric division. Therefore, we can specify that we want to catch only those two `Exception`s, and in addition specify that we want to keep the `Exception` object as the variable `e`. Restricting exception handling in this way avoids masking of errors that we did not anticipate, and which may reflects bugs in our code.


```python
try:
  i = oneover(0)
except (TypeError, ZeroDivisionError) as e:
  print('A problem occurred: %s' % e)
```


### Re-raising (from)

We can also pass the `Exception` on after catching it, by doing a blank `raise`.


```python
# should-raise
try:
  i = oneover(0)
except ZeroDivisionError as e:
  print('Oops!')
  raise
```


Or you can do a `raise … from` (Python 3 only).


```python
# should-raise
try:
    i = oneover(0)
except ZeroDivisionError as e:
    raise ValueError('Cannot divide by zero') from e
```


### else … finally …

The `else` block of a `try … except …` is executed when *no* `Exception` occurred during the `try` block. And finally there is a `finally` block, which is always executed, regardless of whether or not an `Exception` occurred; this can be used to perform clean-up operations etc.


```python
try:
    i = oneover('x')
except ZeroDivisionError as e:
    print('Cannot divide by zero')
except TypeError as e:
    print('Expecting a non-zero number')
else:
    print('No exception occurred')
finally:
    print('This is always executed')
```


## Raising Exceptions

You can raise `Exception`s yourself to indicate that something went wrong. It is good practice to use Python's built-in `Exception` objects whenever this makes sense.

```python
# should-raise
def factorial(n):

    if n < 0:
        raise ValueError('Factorial expects non-negative integers')
    return 1 if n == 0 else n*factorial(n-1)


factorial(-1)
```


But you can also create custom `Exception` objects.


```python
# should-raise
class FactorialError(Exception): pass


def factorial(n):

    if n < 0:
        raise FactorialError('Factorial expects non-negative integers')
    return 1 if n == 0 else n*factorial(n-1)


factorial(-1)
```


## Exercises

<div class='info-box' markdown=1>

### An interactive calculator

%-- include: exercises/basic/exceptions.md --%

[View solution](%url:exceptions%-solution)

</div>
