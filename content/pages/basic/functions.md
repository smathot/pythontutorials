title: Functions
next_title: Modules
next_url: %url:modules%

This tutorial contains five interactive mini exercises and two review exercises. Try to solve them all!


[TOC]


## Functions: what and why?

A *function* is a re-usable code block, typically with a name. The main goal of functions is to avoid duplication of code. Another important goal of functions is to divide code into parts with clearly defined functions; doing so can drastically improve the readability of your code.

Say that you want to turn a string with multiple words into an acronym, such that '<b>a</b> <b>c</b>oded <b>r</b>endition <b>o</b>f <b>n</b>ames <b>y</b>ielding <b>m</b>eaning' becomes 'ACRONYM'. You can do that by first splitting the string into separate words, iterating through the resulting list of words, turning the first letter of each word to uppercase, and concatening each first letter to a new string that, in the end, contains the acronym.

```python
words = 'a coded rendition of names yielding meaning'
acronym = ''
for word in words.split():
  acronym += word[0].upper()
print(acronym)
```

So far there is no code duplication, and hence no real need for a function. But now say that you want to do *almost* the same thing again for another string: 'New York City'. To do this without a function, we would have to copy-paste our code, resulting in code duplication:


```python
words = 'a coded rendition of names yielding meaning'
acronym = ''
for word in words.split():
  acronym += word[0].upper()
print(acronym)
words = 'New York City'
acronym = ''
for word in words.split():
  acronym += word[0].upper()
print(acronym)
```

When you see this kind of code duplication, then you know that a function is likely to improve your code. Let's see, step by step, how we can accomplish this.


## def: defining a function

A function is defined with the `def` statement, followed by the name of the function and parentheses. Like any statement that is followed by an indented code block, the statement ends with a colon.

Let's define an `acronym()` function that (for now) determines the acronym for 'a coded rendition of names yielding meaning' and prints out the result. We execute the function by calling its name followed by parentheses.


```python
def acronym():  # Define the function
  words = 'a coded rendition of names yielding meaning'
  s = ''
  for word in words.split():
    s += word[0].upper()
  print(s)


acronym()  # Call the function
```

<div class="exercise" id="exercise_def" markdown="1">
#### Mini exercise

(Following-up from the [`zip()` exercise](%url:loops%).) Define a function named `best_selling_artists` that prints out the [four best-selling artists of all time](https://en.wikipedia.org/wiki/List_of_best-selling_music_artists) and the number of records that they sold, with one line per artist in the following format: 'The Beatles sold 600000000.0 records'.

<textarea class="code height250"></textarea>
<div hidden class="solution_validate">
try:
  correct = callable(best_selling_artists)
except:
  correct = False
</div>
</div>


## Arguments and return values

### Function arguments

The `acronym()` function defined above is not very useful, because it lacks flexibility. It determines an acronym but *only* for the string 'a coded rendition of names yielding meaning', which is hard-coded into the function. To make the function more flexible, you can add *arguments* (or *parameters*). That is, you pass one or more variables to the function, and the function then performs some operation on or with these variables.


```python
def acronym(words):
  s = ''
  for word in words.split():
    s += word[0].upper()
  print(s)


acronym('do it yourself')
```

<div class="exercise" id="exercise_args" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists`. This time, let the function accept a single argument named `artist` and print the number of record sales for this artist in the following format: 'The Beatles sold 600000000.0 records'. If the artist is not known, use 0 for the number of record sales. (Tip: use a `dict` with artists as keys and record sales as values.)

<textarea class="code height250"></textarea>
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

Function arguments can have default values, so that you can, but do not have to, pass these arguments. Such arguments with default values are called *keywords*. We can redefine `acronym()` such that `words` is a keyword that has an empty string as a default value (for which the acronym is also an empty string).


```python
def acronym(words=''):
  s = ''
  for word in words.split():
    s += word[0].upper()
  print(s)


acronym()
```

<div class="exercise" id="exercise_keywords" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists` that takes a single argument named `artist`. The function is identical to that of the previous mini exercise, except that `artist` should now have a default value of `None`. If no value for artist is specified when calling the function, the function should ask the user to enter an artist name using the `input()` function.

<textarea class="code height250"></textarea>
<div hidden class="solution_validate">
def input():
  return 'dummy'
old_input = __builtins__.input
__builtins__.input = input
try:
  best_selling_artists()
  best_selling_artists(artist='Madonna')
  correct = True
except:
  correct = False
__builtins__.input = old_input
</div>
</div>


### Return values

Many functions also have *return values*; that is, they communicate a value back to where they were called from. We can redefine `acronym()` such that it doesn't print the acronym directly, but rather `return`s it.


```python
def acronym(words=''):
  s = ''
  for word in words.split():
    s += word[0].upper()
  return s


ikea = acronym('Ingvar Kamprad Elmtaryd Agunnaryd')
print(ikea)
```

<div class="exercise" id="exercise_return" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists` that takes a single argument named `artist` with a default value of `None`. The function is identical to that of the previous mini exercise, except that the number of record sales should now be returned, rather than printed out.

<textarea class="code height250"></textarea>
<div hidden class="solution_validate">
def input():
  return 'dummy'
old_input = __builtins__.input
__builtins__.input = input
import operator
correct = True
try:
  if best_selling_artists() != 0:
    correct = False
  if not operator.gt(best_selling_artists(artist='Madonna'), 100000):
    correct = False
except:
  correct = False
__builtins__.input = old_input
</div>
</div>

## Docstrings

A documentation string, or *docstring*, is a `str` that directly follows the `def` line. This allows you to describe what the function does. In most cases, a docstring will be a multiline string. It is best practice to document all but the most trivial functions with a clear docstring!


```python
def acronym(words=''):
  """Determines the acronym for a string."""
  s = ''
  for word in words.split():
    s += word[0].upper()
  return s
```

<div class="exercise" id="exercise_docstring" markdown="1">
#### Mini exercise

As before, define a function named `best_selling_artists` that takes a single argument named `artist` with a default value of `None` and returns the number of record sales. Add a docstring to the function that concisely describes what the function does.

<textarea class="code height250"></textarea>
<div hidden class="solution_validate">
try:
  correct = callable(best_selling_artists) and best_selling_artists.__doc__ is not None
except:
  correct = False
</div>
</div>


## Functions that call functions

Most programs consist of functions that call other functions that call yet other functions, etc. For example, we could define a function called `acronyms()` that takes a list of sentences, where each sentence is itself a string of multiple words, and return a list of corresponding acronyms.


```python
def acronym(words=''):
  """Determines the acronym for a string."""
  s = ''
  for word in words.split():
    s += word[0].upper()
  return s


def acronyms(sentences=[]):
  """Determines the acronyms for a list of strings"""
  l = []
  for words in sentences:
    l.append(acronym(words))
  return l
  
  
l = acronyms(['a coded rendition of names yielding meaning',
              'do it yourself',
              'new york city',
              'Ingvar Kamprad Elmtaryd Agunnaryd'])
print(l)
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
