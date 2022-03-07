title: Modules
next_title: Exceptions
next_url: %url:exceptions%

This tutorial contains two interactive mini exercises and two review exercises. Try to solve them all!

[TOC]


## The Python standard library

So far, we've only used functions that are built into Python, and that you can use straight away when you start a Python interpreter. However, you can `import` modules to get additional functionality. Many common modules are included in Python by default so that you don't need to install them—but you do have to `import` them! These modules make up the Python standard library:

- <https://docs.python.org/3/library/index.html>


## `import`: importing modules

Let's consider the `random` module:

- <https://docs.python.org/3/library/random.html>

The `random` module contains many functions for randomization. For example, `random.choice()` takes an iterable, such as a `list`, and returns a single, randomly selected element. To use `random.choice()`, you need to `import` the `random` module.


```python
# Preferred
import random
prime_numbers = [1, 3, 5, 7, 11]
print(random.choice(prime_numbers))
```

In the example above, you import the entire `random` module and then selectively call `random.choice()`. However, the `import` statement is flexible and allows you to import modules and functions in many different ways. These all have their place, but as a general rule, the `import` method shown above is clearest and therefore preferred.


<div class="exercise" id="exercise_import" markdown="1">
#### Mini exercise

Import the `string` module, and print out [all ASCII letters](https://docs.python.org/3/library/string.html#string.ascii_letters) as defined in this module.

<textarea class="code"></textarea>
<div hidden class="solution_output">abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ</div>
</div>

You can also selectively import the `choice()` function. The downside of this way of importing is that you cannot easily tell anymore that `choice()` is part of the `random` module.


```python
# Not preferred
from random import choice
print(choice(prime_numbers))
```

<div class="exercise" id="exercise_import_from" markdown="1">
#### Mini exercise

Selectively import the `sample()` function from the `random` module, and the `ascii_letters` attribute of the `string` module. Use these to randomly sample five letters and assign these to a variable called `five_letters`.

<textarea class="code"></textarea>
<div hidden class="solution_validate">
import random
import string
correct = 1
try:
    if random.sample is not sample:
        correct = 0
    if string.ascii_letters is not ascii_letters:
        correct = 0
    if len(five_letters) != 5:
        correct = 0
except:
    correct = 0
</div>
</div>


You can also directly import everything from the `random` module: a *wildcard* import. This is generally considered bad practice, because it makes it difficult to tell where a function comes from.


```python
# Not preferred
from random import *
print(choice(prime_numbers))
```

Finally, the `import` statement allows you to rename the imported modules or functions. Again, this is generally not preferred because of potential confusion. Exceptions are libraries such as `numpy` for which an import-and-rename (`import numpy as np`) is so common that it is unlikely to result in confusion.


```python
# Not preferred
import random as rnd
print(rnd.choice(prime_numbers))
```


## Review exercises

<div class='exercise no-progress' id='exercise_statistics' markdown=1>

### Some simple statistics

%-- include: exercises/basic/modules-1.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:modules%-solution-1) to see one solution!

<textarea class="code height300"></textarea>

</div>

<div class='exercise no-progress' id='exercise_files' markdown=1>

### Files and folders

%-- include: exercises/basic/modules-2.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:modules%-solution-2) to see one solution!

<textarea class="code height300"></textarea>

</div>
