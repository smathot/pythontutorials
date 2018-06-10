title: Functions


[TOC]


In computer-science, a function is a block of code with a name. The main goal of functions is to make code *re-usable*.

Let's do a little Pythagoras again: Say that you want calculate the length of the long side (`c`) of a right triangle with short sides (`a` and `b`) of length 1. For some reason, you want to do this three times, printing out the result each time.


```python
# Once
a = b = 1
long_side = (a ** 2 + b ** 2) ** .5
print('Long side = {0}'.format(long_side))
# Twice
a = b = 1
long_side = (a ** 2 + b ** 2) ** .5
print('Long side = {0}'.format(long_side))
# Three times
a = b = 1
long_side = (a ** 2 + b ** 2) ** .5
print('Long side = {0}'.format(long_side))
```

## `def`: defining a function

When you see code like above, with so much duplication in it, then you know that a function is likely to improve it. In Python, you define a function with the `def` statement, followed by the name of the function and parentheses. Like any statement that is followed by an indented code block, the line ends with a colon.

Let's define a `pythagoras()` function that (for now) calculates the long side (`c`) of a triangle with short sides (`a` and `b`) of length 1, and prints out the result.


```python
def pythagoras():

    a = b = 1
    long_side = (a ** 2 + b ** 2) ** .5
    print('Long side = {0}'.format(long_side))


pythagoras()
pythagoras()
pythagoras()
```

<div class='info-box' markdown=1>
__Exercise__

Define a function, `count_words()`, that reads a string of user input, splits the string into a list of words (assuming that words are separated by whitespace, using `str.split()`), and prints out the number of words in the string. Then call this function two times.
</div>


## Arguments and return values

### Function arguments

Most functions take one or more *arguments*. That is, you pass one or more variables to the function, and the functions performs some operation on or with these variables. For example:


```python
def pythagoras_2(a, b):

    long_side = (a ** 2 + b ** 2) ** .5
    print('The long side is {0}'.format(long_side))


pythagoras_2(1, 1)
```

<div class='info-box' markdown=1>
__Exercise__

Define the function `count_words_2()` such that it takes a single `str` as an argument, and prints out the number of words in this `str`. Call this function twice with different `str` arguments.
</div>


### Default function arguments (keywords)

Function arguments can have default values, so that you can, but do not have to, pass these arguments. Such arguments with default values are called *keywords*.

We can redefine the Pythagoras function such that the `a` and `b` arguments are keywords with a default value of `1`.


```python
def pythagoras_3(a=1, b=1):

    long_side = (a ** 2 + b ** 2) ** .5
    print('The long side is {0}'.format(long_side))


pythagoras_3()
```

<div class='info-box' markdown=1>
__Exercise__

Define the function `count_words_3()` such that it takes a single `str` as a keyword argument, with a default value of `''` (empty string), and prints out the number of words. Call `count_words_3()` several times with different arguments, and without any argumetns, to see if it works.
</div>


### Return values

Many functions also have *return values*, that is, they communicate a variable back to the location where they calledfrom.

We can redefine the Pythagoras function such that it does not print the length of the long side directly, but rather `return`s it.


```python
def pythagoras_4(a=1, b=1):

    return (a ** 2 + b ** 2) ** .5


long_side = pythagoras_4(1, 1)
print('The long side is {0}'.format(long_side))
```

<div class='info-box' markdown=1>
__Exercise__

Define the function `count_words_4()` such that it takes a single `str` as a keyword argument, with a default value of `''` (empty string), and returns the number of words in the `str`. Call `count_words_4()` several times with different arguments, and without any arguments, and print the return value each time, to see if it works.
</div>


## Docstrings

A documentation string, or *docstring*, is a `str` that directly follows the `def` line. This allows you to describe what the function does. In most cases, a docstring will be a multiline string.

*It is best practice to document all but the most trivial functions with a clear docstring!*


```python
def pythagoras_5(a=1, b=1):    
    """Returns the length of the long side of a right triangle
    given the two short sides a and b.
    """
    return (a ** 2 + b ** 2) ** .5
```
