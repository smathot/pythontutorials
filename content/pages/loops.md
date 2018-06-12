title: Loops: for and while
next_title: Functions
next_url: %url:functions%


[TOC]


## The `for` loop

A `for` loop runs a block of code for each element in an iterable object, such as a `list`. Analogous to the `if` statement, the `for` statement ends with a colon, and the following code block is defined by indentation:


```python
prime_numbers = [1, 3, 5, 7, 11]
for prime in prime_numbers:
    print(prime)
```

If you loop through a `dict`, you loop through its keys. To loop through the keys and the values at the same time, you can use the `dict.items()` function, which returns an iterable of key, value tuples.


```python
ages = {
    'Jay-Z': 47,
    'Emanuel Macron': 40
}
for name, age in ages.items():
    print('{0} is {1} years old'.format(name, age))
```

## The `while` loop

A `while` loop is a way to run a block of code until a particular condition is no longer `True`. The syntax is by now familiar:


~~~ .python
user_input = ''
while user_input != 'quit':
    user_input = input('>>> ')
    print('The user said: {0}'.format(user_input))
~~~


## `continue`: abort one iteration

The `continue` statement, which you can use in `for` and `while` loops (but nowhere else), aborts a single iteration of a loop, and continues with the next iteration. To give an example, you can use `continue` to skip all cities that are not capitals:


```python
cities = ['Berlin', 'São Paulo', 'Tokyo', 'New York']
capitals = ['Berlin', 'Tokyo']
for city in cities:
    if city not in capitals:
        continue
    print('{0} is a capital'.format(city))
```


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


## Useful functions

### range(): iterate through a range of values

`range()` corresponds to a range of numbers. The simplest and most common use case is to specify only a stop value, which is exclusive (i.e. `range(3)` does not include `3`!):

```python
for i in range(3):
  print(i)
```

However, you can also specify a start value and a step size:

```python
from_value = 1
to_value = 4
step_size = 2
for i in range(from_value, to_value, step_size):
  print(i)
```


### enumerate(): iterate and count

`enumerate()` takes an iterable object, and returns another iterable in which each element is paired with a counter variable.

```python
cities = ['Berlin', 'São Paulo', 'Tokyo', 'New York']
for i, city in enumerate(cities):
  print('{0}: {1}'.format(i, city))
```


### zip(): iterate through multiple iterables

`zip()` takes one or more iterable objects, and returns another iterable in which elements from the original iterables are paired. This allows you to iterate through multiple iterables at the same time. The zipped iterable is as long as the shortest of the original iterables.


```python
artists = 'The Beatles', 'Elvis Presley', 'Michael Jackson', 'Madonna'
sales = 600e6, 600e6, 350e6, 300e6
for artist, sold in zip(artists, sales):
  print('{0} sold {1} records'.format(artist, sold))
```


## Exercises

<div class='info-box' markdown=1>

### Fibonacci

Calculate the [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_number) up to 1,000. Print out each Fibonacci number including its position in the series. Like so:

~~~
0: 1
1: 1
2: 2
3: 3
4: 5
etc.
~~~

</div>

<div class='info-box' markdown=1>

### Best-selling artists

Do the following until the user enters `quit`: Ask the name of an artist. Look up the number of sales of this artist in a `dict`, and print out the result if this number is known. If the number of sales is unknown, ask the user to enter the number of sales, and update the `dict` accordingly.

</div>
