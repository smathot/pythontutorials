title: Functions
next_title: Modules
next_url: %url:modules%

This tutorial contains five interactive mini exercises and two review exercises. Try to solve them all!


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

<div class="exercise" id="exercise_def" markdown="1">
#### Mini exercise

(Following-up from the [`zip()` exercise](%url:loops%).) Define a function named `best_selling_artists` that prints out the [four best-selling artists of all time](https://en.wikipedia.org/wiki/List_of_best-selling_music_artists) and the number of records that they sold, with one line per artist in the following format: 'The Beatles sold 600000000.0 records'.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
try:
  correct = callable(best_selling_artists)
except:
  correct = False
</div>
</div>


## Arguments and return values

### Function arguments

The `pythagoras()` function defined above is not very useful, because it lacks flexibility. It calculates the long side `c`, but *only* for short sides `a = 1` and `b = 1`. To make the function more flexible, you can add *arguments*. That is, you pass one or more variables to the function, and the function then performs some operation on or with these variables.


```python
def pythagoras(a, b):

  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


pythagoras(1, 1)
```

<div class="exercise" id="exercise_args" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists`. This time, let the function accept a single argument named `artist` and print the number of record sales for this artist in the following format: 'The Beatles sold 600000000.0 records'. If the artist is not known, use 0 for the number of record sales.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
correct = True
try:
  best_selling_artists(artist='boef')
  best_selling_artists(artist='Madonna')
except:
  correct = False
</div>
</div>

### Default function arguments (keywords)

Function arguments can have default values, so that you can, but do not have to, pass these arguments. Such arguments with default values are called *keywords*. We can redefine `pythagoras()` such that the `a` and `b` arguments are keywords with a default value of `1`.


```python
def pythagoras(a=1, b=1):

  c = (a ** 2 + b ** 2) ** .5
  print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


pythagoras()
```

<div class="exercise" id="exercise_keywords" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists` that takes a single argument named `artist`. The function is identical to that of the previous mini exercise, except that `artist` should now have a default value of `None`. If no value for artist is specified when calling the function, the function should ask the user to enter an artist name using the `input()` function.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
try:
  best_selling_artists()
  best_selling_artists(artist='Madonna')
  correct = True
except:
  correct = False
</div>
</div>


### Return values

Many functions also have *return values*, that is, they communicate a value back to where they were called from. We can redefine `pythagoras()` such that it doesn't print the length of the long side directly, but rather `return`s it.


```python
def pythagoras(a=1, b=1):

  return (a ** 2 + b ** 2) ** .5


a = b = 1
c = pythagoras(a, b)
print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
```

<div class="exercise" id="exercise_return" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists` that takes a single argument named `artist` with a default value of `None`. The function is identical to that of the previous mini exercise, except that the number of record sales should now be returned, rather than printed out.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
try:
  best_selling_artists() is not None
  best_selling_artists(artist='Madonna') is not none
  correct = True
except:
  correct = False
</div>
</div>

## Docstrings

A documentation string, or *docstring*, is a `str` that directly follows the `def` line. This allows you to describe what the function does. In most cases, a docstring will be a multiline string. It is best practice to document all but the most trivial functions with a clear docstring!


```python
def pythagoras(a=1, b=1):    
    """Returns the length of the long side of a right triangle
    given two short sides a and b.
    """
    return (a ** 2 + b ** 2) ** .5
```

<div class="exercise" id="exercise_docstring" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists` that takes a single argument named `artist` with a default value of `None` and returns the number of record sales. Add a docstring to the function that concisely describes what the function does.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
try:
  correct = callable(best_selling_artists) and best_selling_artists.__doc__ is not None
except:
  correct = False
</div>
</div>


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


## Review exercises

<div class='exercise no-progress' id='exercise_factorial_for' markdown=1>

### Factorial using for

%-- include: exercises/basic/functions-1.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:functions%-solution-1) to see one solution!

<textarea class="code height300"></textarea>

</div>

<div class='exercise no-progress' id='exercise_factorial_recursion' markdown=1>

### Factorial using recursion

%-- include: exercises/basic/functions-2.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:functions%-solution-2) to see one solution!

<textarea class="code height300"></textarea>

</div>
