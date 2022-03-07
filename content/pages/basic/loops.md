title: Loops: for and while
next_title: Functions
next_url: %url:functions%


This tutorial contains seven interactive mini exercises and two review exercises. Try to solve them all!


[TOC]


## The for loop

A `for` loop executes a code block for each element in an iterable, such as a `list`, `tuple`, or `set`. Analogous to the `if` statement, the `for` statement ends with a colon, and the to-be-looped code block is defined by indentation:


```python
prime_numbers = [1, 3, 5, 7, 11]
for prime in prime_numbers:
    # This is inside the loop because it is indented
    print(prime)
# This is after the loop because it is no longer indented
print('Done!')
```

If you iterate (loop) through a `dict`, you iterate through its keys. To iterate through the keys and the values at the same time, you can use `dict.items()` function, which returns an iterable of (key, value) tuples.


```python
ages = {
    'Jay-Z': 52,          # and counting
    'Emanuel Macron': 44  # and counting
}
for name, age in ages.items():
    print(f'{name} is {age} years old')
```

<div class="exercise" id="exercise_for" markdown="1">
#### Mini exercise

You can also loop through a `str`, in which case you get individual characters as if you were looping through a `list` of characters. Use a `for` loop through loop through a `str` with the first five letters of the alphabet. Print out each character on a separate line. After the loop, print out 'Done!'

<textarea class="code"></textarea>
<div hidden class="solution_output">
a
b
c
d
e
Done!
</div>
</div>

## The while loop

A `while` loop executes a code block until a particular condition is no longer `True`.


~~~ .python
user_input = ''
while user_input != 'quit':
    user_input = input('>>> ')
    print(f'The user said: {user_input}')
print('Quitting ...')
~~~

__Output:__

~~~
>>> Hello!
The user said: Hello!
>>> quit
The user said: quit
Quitting ...
~~~


<div class="exercise" id="exercise_while" markdown="1">
#### Mini exercise

Create a simple calculator for additions! Repeatedly ask the user to enter numbers. Each time that the user provides input, this input is first converted to `float` and then added to a running total (which should start from 0). When the user enters 'add', the `loop` stops and the running total is printed out.

When running the code, enter '3', '2', '1', and 'add' to solve the exercise.

<textarea class="code height200"></textarea>
<div hidden class="solution_output">6.0</div>
</div>

## continue: abort one iteration

The `continue` statement, which you can use in `for` and `while` loops (but nowhere else), aborts a single iteration of a loop, and continues with the next iteration. To give an example, you can use `continue` to skip all cities that are not capitals:


```python
cities = ['Berlin', 'São Paulo', 'Tokyo', 'New York']
capitals = ['Berlin', 'Tokyo']
for city in cities:
  # If the current city is not a capital, continue with the next city
  if city not in capitals:
    continue
  print(f'{city} is a capital')
```

<div class="exercise" id="exercise_continue" markdown="1">
#### Mini exercise

Loop through the `list` of four cities above. Use `continue` to ignore cities that have a space in the name. Print out the other city names. (Tip: You can use `in` to check whether one string is a substring of another string.)

<textarea class="code height150"></textarea>
<div hidden class="solution_output">
Berlin
Tokyo
</div>
</div>

## break: abort a loop

The `break` statement is similar to the `continue` statement, but aborts the loop entirely, rather than just aborting the current iteration. To give an example, you can use `break` to print out all prime numbers below `10`.


```python
for prime in prime_numbers:
  # Abort the loop when we reach a number that is 10 or higher
  if prime >= 10:
    break
  print(prime)
```

<div class="exercise" id="exercise_break" markdown="1">
#### Mini exercise

Loop through the `list` of four cities above. Print out the name of each city. Use `break` to stop after Tokyo.

<textarea class="code height150"></textarea>
<div hidden class="solution_output">
Berlin
São Paulo
Tokyo
</div>
</div>


## Useful functions

### range(): iterate through a range of values

`range()` corresponds to a range of numbers. The simplest and most common use case is to specify only a stop value, which is exclusive (i.e. `range(3)` does not include `3`!):

```python
for i in range(3):
  print(i)
```

However, you can also specify a start value and a step size (negative step sizes allow you to count backwards):

```python
from_value = 1
to_value = 4
step_size = 2
for i in range(from_value, to_value, step_size):
  print(i)
```

<div class="exercise" id="exercise_range" markdown="1">
#### Mini exercise

Use `range()` to count down from 5 to 1, printing each number on a separate line. After the loop, print 'Go!'.

<textarea class="code"></textarea>
<div hidden class="solution_output">
5
4
3
2
1
Go!
</div>
</div>


### zip(): iterate through multiple iterables

`zip()` takes one or more iterables, and returns a zipped iterable in which elements from the original iterables are paired. This allows you to iterate through multiple iterables at the same time. The zipped iterable is as long as the shortest of the original iterables.


```python
# Source: https://en.wikipedia.org/wiki/List_of_best-selling_music_artists
artists = 'The Beatles', 'Elvis Presley', 'Michael Jackson', 'Madonna'
sales = 600e6, 600e6, 350e6, 300e6
for artist, sold in zip(artists, sales):
  print(f'{artist} sold {sold} records'.format(artist, sold))
```

<div class="exercise" id="exercise_zip" markdown="1">
#### Mini exercise

Use one `range()` to count down from 0 to 4, and another `range()` to count up from 4 to 0. Use `zip()` to loop through both ranges together. Print each pair of numbers out on a separate line in this format: '0 4', etc.

<textarea class="code height150"></textarea>
<div hidden class="solution_output">
0 4
1 3
2 2
3 1
4 0
</div>
</div>


### enumerate(): iterate and count

`enumerate()` takes an iterable, and returns another iterable in which each element is paired with a counter variable.

```python
cities = ['Berlin', 'São Paulo', 'Tokyo', 'New York']
for i, city in enumerate(cities):
  print(f'{i}: {city}')
```

<div class="exercise" id="exercise_enumerate" markdown="1">
#### Mini exercise

Use `range()` to count down from 4 to 0. Use `enumerate()` to create another counter that goes for 0 to 4. Print each pair of numbers out on a separate line in this format: '0 4', etc. (I.e. the result is the same as for the previous mini exercise, but the implementation is different.)

<textarea class="code height150"></textarea>
<div hidden class="solution_output">
0 4
1 3
2 2
3 1
4 0
</div>
</div>


## Review exercises

<div class='exercise no-progress' id='exercise_fibonacci' markdown=1>

### Fibonacci

%-- include: exercises/basic/loops-1.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:loops%-solution-1) to see one solution!

<textarea class="code height300"></textarea>

</div>

<div class='exercise no-progress' id='exercise_artists' markdown=1>

### Best-selling artists

%-- include: exercises/basic/loops-2.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:loops%-solution-2) to see one solution!

<textarea class="code height300"></textarea>

</div>
