title: Exceptions: error handling


This tutorial contains three interactive mini exercises and one review exercise. Try to solve them all!


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
  return 1 / i
```

Calling `oneover(0)` results in a `ZeroDivisionError` (a special kind of `Exception`) because dividing any number by `0` is not allowed:

```python
# should-raise
oneover(0)
```

<div class="exercise" id="exercise_exception" markdown="1">
#### Mini exercise

A `ValueError` is a special kind of `Exception` that is raised when a function is called with an argument that has the correct type but an incorrect value. Trigger a `ValueError ` by trying to convert the string 'this is not an int' to an `int`.

<textarea class="code"></textarea>
<div hidden class="solution_output">invalid literal for int() with base 10: 'this is not an int'</div>
</div>


## Handling `Exception`s

### try … except …

Now let's use a `try … except …` statement to safely catch `Exception`s.

```python
try:
  i = oneover(0)
except:  # A blank except is not good practice!
  print('Some problem occurred')
print("I'm still alive!")
```

In the example above, if any `Exception` occurs in the block that follows the `try` statement, then the execution of that block is terminated, and the `except` block is executed. Importantly, however, the code continues to run; that is, `try … except …` statements allow you to deal with `Exception`s gracefully.

It is good practice to specify *which* `Exception`s should be caught. For example, `oneover()` triggers a `ZeroDivisionError` error when called with `0` and a `TypeError` called it with a `str` or some other value that doesn't work in a numeric division. Therefore, we can specify that we want to catch only those two `Exception`s, and in addition specify that we want to keep the `Exception` object as the variable `e`. Restricting exception handling in this way avoids masking of errors that we did not anticipate, and which may reflects bugs in our code.


```python
try:
  i = oneover(0)
except (TypeError, ZeroDivisionError) as e:
  print('A problem occurred: %s' % e)
```

You can also handle specify a different way to handle each different kind of `Exception` by having multiple `except` blocks:


```python
try:
  i = oneover(0)
except TypeError:
  # This will be executed when a TypeError is raised
  print('oneover() expects a float or int')
except ZeroDivisionError:
  # This will be executed when a ZeroDivisionError is raised
  print('oneover() cannot be called with 0')
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

<div class="exercise" id="exercise_except" markdown="1">
#### Mini exercise

Create a function called `safe_int()` that takes a single argument `i`. If possible, the function converts `i` to `int` and returns it. If not possible (i.e. if an `Exception` occurs), the function returns `None`.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
correct = 1
try:
  if safe_int('10') != 10:
    correct = 0
  if safe_int('x') is not None:
    correct = 0
except:
  correct = 0
</div>
</div>


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


But you can also create custom `Exception` objects. This allows you to communicate clearly to the user what kind of error occurred.


```python
# should-raise
class FactorialError(Exception): pass


def factorial(n):

    if n < 0:
        raise FactorialError('Factorial expects non-negative integers')
    return 1 if n == 0 else n*factorial(n-1)


factorial(-1)
```


<div class="exercise" id="exercise_raise" markdown="1">
#### Mini exercise

Define a function `capitalize_last_name()` that accepts as argument a string with a (single) first and a (single) last name, and returns a string in which only the first letter of the first name is uppercase, whereas all letters of the last name are uppercase; in otherwords, 'marisa tomei' becomes 'Marisa TOMEI'. (Tip: use `str.split()` to split a `str` into separate words.)

If something other than a `str` object is passed as an argument, the function should raise a `TypeError`. (Tip: you can use `isistance()` to check whether an object is of a particular type.) If the `str` does not consist of exactly two words, the function should raise a `ValueError`.

<textarea class="code"></textarea>
<div hidden class="solution_validate height250">
correct = 1
try:
  if capitalize_last_name('marisa tomei') != 'Marisa TOMEI':
    correct = 0
  try:
    capitalize_last_name('marisa')
  except ValueError:
    pass
  else:
    correct = 0
  try:
    capitalize_last_name(0)
  except TypeError:
    pass
  else:
    correct = 0
except:
  correct = 0
</div>
</div>


## Review exercise

<div class='exercise no-progress' id='exercise_calculator' markdown=1>

### An interactive calculator

%-- include: exercises/basic/exceptions.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:exceptions%-solution) to see one solution!

<textarea class="code height300"></textarea>

</div>

This concludes the Python Basics course. Congratulations—you made it to the finish!

<div>
<a class='btn btn-success btn-large btn-block' href='/'>Go back to the home page</a></p>
</div>
