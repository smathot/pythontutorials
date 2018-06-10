title: Loops


[TOC]


## The `for` loop

A `for` loop is a way to run a block of code for each element in an iterable object, such as a `list`. Just as the `if` statement, the `for` statement ends with a colon, and the followed code block is defined by indentation:


```python
prime_numbers = [1, 3, 5, 7, 11]
for prime in prime_numbers:
    print(prime)
```

If you loop through a `dict`, you loop through its keys. To loop through the keys and the values at the same time, you can use the `dict.items()` function, which loops over key, value tuples.


```python
people_with_ages = {
    'Jay-Z' : 47,
    'Emanuel Macron' : 40
}
for name, age in people_with_ages.items():
    print('{0} is {1} years old'.format(name, age))
```


<div class='info-box' markdown=1>
__Exercise__

Loop through all odd numbers, raise them to the power of two, create a new `list` called `power_2` containing the resulting numbers, and print out this new list.
</div>


## The `while` loop

A `while` loop is a way to run a block of code until a particular condition is no longer `True`. The syntax is by now familiar:


```python
i = 0
while i < 5:
    print(i)
    i += 1 # A shortcut for i = i + 1
```

<div class='info-box' markdown=1>
__Exercise__

Remove (`pop()`) elements from `power_2` and print them out, until `power_2` is empty. Make use of the fact that an empty `list` equals `False` whereas a non-empty `list` equals `True`.
</div>


## `continue`: abort one iteration

The `continue` statement, which you can use in `for` and `while` loops (but nowhere else), aborts a single iteration of a loop, and continues with the next iteration. To give an example, you can use `continue` to skip all cities that are not capitals:


```python
CITIES = ['Berlin', 'São Paulo', 'Tokyo', 'New York']
CAPITALS = ['Berlin', 'Tokyo']
for city in CITIES:
    if city not in CAPITALS:
        continue
    print('{0} is a capital'.format(city))
```

<div class='info-box' markdown=1>
__Exercise__

Define a `list` of your friends' names. Loop through this list, and use `continue` to print out only those that do not start with a vowel.
</div>


## `break`: abort a loop

The `break` statement is similar to the `continue` statement, but aborts the loop entirely, rather than just aborting the current iteration. To give an example, you can use `break` to print out all prime numbers below `10`.


```python
for prime in prime_numbers:
    # Abort the loop when we reach a number that is 10 or higher
    if prime >= 10:
        break
    print(prime)
```

<div class='info-box' markdown=1>
__Exercise__

Take the `list` of your friend's names. One of these friends is now your BFF (best friend forever). Loop through the `list` of names, and use `break` to print the names out until you've found the name of your BFF.
</div>
