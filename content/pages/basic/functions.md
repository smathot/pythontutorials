title: Functions
next_title: Modules
next_url: %url:modules%


[TOC]


## Functions: what and why?

A *function* is a re-usable code block, typically with a name. The main goal of functions is to avoid duplication of code. Another important goal of functions is to divide code into parts with clearly defined functions; doing so can drastically improve the readability of your code.

Say that you want calculate the length of the long side `c` of a right triangle with short sides `a` and `b`, using [Pythagoras' theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem). And say that you have a list (`some_triangles`) of `a, b` tuples, which you can easily iterate through to determine the corresponding long sides `c`.


```python
some_triangles = (1, 1), (1, 2), (2, 2)
for a, b in some_triangles:
  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
```

So far there is no code duplication, and hence no real need for a function. But now say that you want to do *almost* the same thing again, for another `list` (`more_triangles`) of `a, b` tuples. To do this without a function, we would have to copy-paste our code, resulting in code duplication:


```python
some_triangles = (1, 1), (1, 2), (2, 2)
for a, b in some_triangles:
  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
more_triangles = (3, 3), (3, 4), (4, 4)
for a, b in more_triangles:
  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
```


When you see this kind of code duplication, then you know that a function is likely to improve your code. Let's see, step by step, how we can accomplish this.


## def: defining a function

A function is defined with the `def` statement, followed by the name of the function and parentheses. Like any statement that is followed by an indented code block, the statement ends with a colon.

Let's define a `pythagoras()` function that (for now) calculates the long side (`c`) of a triangle with short sides (`a` and `b`) of length 1, and prints out the result. We execute the function by calling its name followed by parentheses.


```python
def pythagoras():

    a = b = 1
    c = (a ** 2 + b ** 2) ** .5
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


pythagoras() # Call the function
```


## Arguments and return values

### Function arguments

The `pythagoras()` function defined above is not very useful, because it lacks flexibility. It calculates the long side `c`, but *only* for short sides `a = 1` and `b = 1`. To make the function more flexible, you can add *arguments*. That is, you pass one or more variables to the function, and the function then performs some operation on or with these variables.


```python
def pythagoras(a, b):

  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


pythagoras(1, 1)
```


### Default function arguments (keywords)

Function arguments can have default values, so that you can, but do not have to, pass these arguments. Such arguments with default values are called *keywords*. We can redefine `pythagoras()` such that the `a` and `b` arguments are keywords with a default value of `1`.


```python
def pythagoras(a=1, b=1):

  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


pythagoras()
```


### Return values

Many functions also have *return values*, that is, they communicate a value back to where they were called from. We can redefine `pythagoras()` such that it doesn't print the length of the long side directly, but rather `return`s it.


```python
def pythagoras(a=1, b=1):

  return (a ** 2 + b ** 2) ** .5


a = b = 1
c = pythagoras(a, b)
print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
```


## Docstrings

A documentation string, or *docstring*, is a `str` that directly follows the `def` line. This allows you to describe what the function does. In most cases, a docstring will be a multiline string. It is best practice to document all but the most trivial functions with a clear docstring!


```python
def pythagoras(a=1, b=1):    
    """Returns the length of the long side of a right triangle
    given two short sides a and b.
    """
    return (a ** 2 + b ** 2) ** .5
```


## Functions that call functions

Most programs consist of functions that call other functions that call yet other functions, etc. Returning to the example that we started with, we could rewrite this code to make use of functions, thus avoiding duplication and making the logic of the code clearer.


```python
def pythagoras(a=1, b=1):
  """Returns the length of the long side of a right triangle
  given two short sides a and b.
  """
  return (a ** 2 + b ** 2) ** .5


def print_long_sides(short_sides):
  """Takes a list of (a, b) tuples, corresponding to the short
  sides of a right triangle, and prints out the corresponding
  long side (c).
  """
  for a, b in short_sides:
    c = pythagoras(a, b)
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


some_triangles = (1, 1), (1, 2), (2, 2)
more_triangles = (3, 3), (3, 4), (4, 4)
print_long_sides(some_triangles)
print_long_sides(more_triangles)
```


## Exercises

<div class='info-box' markdown=1>

### Factorial using for

%-- include: exercises/basic/functions-1.md --%

[View solution](%url:functions%-solution-1)

</div>

<div class='info-box' markdown=1>

### Factorial using recursion

%-- include: exercises/basic/functions-2.md --%

[View solution](%url:functions%-solution-2)

</div>
