title: Modules


So far, we've only used functions that are built into Python, and that you can use straight away when you start a Python interpreter. However, you can `import` modules to get additional functionality. Many common modules are included in Python by default so that you don't need to install them explicitly; these make up the Python standard library:

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

In the example above, we import the entire `random` module and then selectively call the `random.choice()` function. However, the `import` statement is very flexible and allows you to import modules and functions in many different ways. These all have their place, but as a general rule, the `import` method shown above is clearest and therefore preferred.

We can also selectively import the `choice()` function. The downside of this way of importing is that we cannot easily tell anymore that `choice()` is part of the `random` module.


```python
# Not preferred
from random import choice
print(choice(prime_numbers))
```

We can also directly import everything from the `random` module: a *wildcard* import. This is generally considered bad practice, because it makes it entirely unclear where functions come from.


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


<div class='info-box' markdown=1>
__Exercise__

Use the `statistics` module to calculate the mean of all prime numbers below 10. Print out the result.
</div>
