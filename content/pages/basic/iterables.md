title: Iterables: list, dict, tuple, and set
next_title: Loops
next_url: %url:loops%

This tutorial contains eight interactive mini exercises and two review exercises. Try to solve them all!

[TOC]


## Iterables, order, and mutability

In Python, an *iterable* object (or simply an *iterable*) is a collection of elements that you can loop (or *iterate*) through one element at a time. Simply put, an iterable is a list-like (or array-like) object. There are many kinds of iterables, which differ in many ways, including whether they are ordered and mutable:

- An iterable is *ordered* if you can retrieve its elements in a *predictable order*
- An iterable is *mutable* if you can change which elements it contains

Python has four built-in iterable types: `list`, `dict`, `tuple`, and `set`


## list: an ordered, mutable collection of elements

A `list` consists of zero or more other elements in a fixed order. The elements of a `list` can be anything, such a numbers (`int`), strings (`str`), and even other `list`s. Different elements from the same `list` can have different types.

A `list` is defined as a comma-separated list of values between square brackets:


```python
prime_numbers = [1, 3, 5, 7, 11]
print(prime_numbers)
empty_list = []
print(empty_list)
```

<div class="exercise" id="exercise_list" markdown="1">
#### Mini exercise

Print a `list` that contains the first three letters of the alphabet as three separate elements.

<textarea class="code"></textarea>
<div hidden class="solution_output">['a', 'b', 'c']</div>
</div>


### Getting a single element (indexing)

To get a single element from a `list`, use the *index* (position) of the element, where `0` is the first element, `1` is the second element, etc. That is, Python uses [zero-based indexing](https://en.wikipedia.org/wiki/Zero-based_numbering). You can also count from the end of the `list` by using a negative index, where `-1` is the last element, `-2`, is the second-to-last element, etc.


```python
print('First prime number:')
print(prime_numbers[0])
print('Last prime number (of our list):')
print(prime_numbers[-1])
```

<div class="exercise" id="exercise_index" markdown="1">
#### Mini exercise

Create a `list` that contains the first five prime numbers. Print out the second number from this list.

<textarea class="code"></textarea>
<div hidden class="solution_output">3</div>
</div>

### Getting a range of elements (slicing)

You can also get multiple elements from a `list` by specifying a *slice*.


```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
from_index = 0
to_index = 4 # Non-inclusive, so until and including 'd' (at index 3)
in_steps_of = 3
print(letters[from_index:to_index:in_steps_of])
```

All the parts of a slice are optional, and fall back to the start of the list (for `from_index`), the end of the list (for `to_index`), and steps of 1. So you can get the first two prime numbers by only specifying the `to_index`, like this:


```python
print(prime_numbers[:2])
```

A common way to create a copy of a list to get the *full slice*. (This is equivalent to `list.copy()` in Python 3.)

```python
my_copy = prime_numbers[:]
```

<div class="exercise" id="exercise_slice" markdown="1">
#### Mini exercise

Again create a `list` that contains the first five prime numbers. Print out a slice that contains all numbers from this `list` except for the first and the last one.

<textarea class="code"></textarea>
<div hidden class="solution_output">[3, 5, 7]</div>
</div>

### len(): counting the number of elements

`len()` counts how many elements there are in a `list`, or more generally in any iterable that has a length. (Some special iterables have no length, for example because they correspond to an infinite series. However, all iterables that we consider here have a length.)


```python
n = len(prime_numbers)
print('We have defined {0} prime numbers'.format(n))
```


### in: checking whether an iterable contains an element

Python has a special operator, `in`, to check whether an element is part of a `list` or another iterable.


```python
if 3 in prime_numbers:
    print('Three is prime')
```

<div class="exercise" id="exercise_in" markdown="1">
#### Mini exercise

Again create a `list` with the first five prime numbers. Ask the user for input. Convert this input to `int`, and check whether the resulting number is in our list of prime numbers. If it is, print out 'The number is prime', else print out 'The number is not among the first five prime numbers'. When running the code, enter one of the first five prime numbers to solve the exercise.

<textarea class="code"></textarea>
<div hidden class="solution_output">The number is prime</div>
</div>

### Modifying a list

A `list` has several common functions for adding or removing elements:

- `list.append(element)` adds an element to the end
- `list.insert(index, element)` inserts an element at position `index`
- `element = list.pop()` removes the last element from the list and returns it. You can also specify an index of an element, in which case this element is removed and returned (instead of the last element).


```python
prime_numbers = []
prime_numbers.append(1)
prime_numbers.append(3) # Etc.
print(prime_numbers)
```

For an overview of `list` functions, see:

- <https://docs.python.org/3.6/tutorial/datastructures.html#more-on-lists>

<div class="exercise" id="exercise_pop" markdown="1">
#### Mini exercise

Again create a `list` with the first five prime numbers. Remove the third number from the list, using either `pop()` or `remove()`. Print out the resulting `list`.

<textarea class="code"></textarea>
<div hidden class="solution_output">[1, 5, 7, 11]</div>
</div>


## dict: an unordered, mutable collection of key-value pairs

A `dict` consists of zero or more key-value pairs. That is, each element of a `dict` is a combination of a value that serves as a key and that is associated with another value. A `dict` is *unordered*, which means that if you iterate through the elements of a `dict`, you are not guaranteed to get the elements in a particular order. So never rely on the order of a `dict`!

A `dict` supports `len()` and `in`, as described above for `list`s. However, indexing a `dict` works differently from a `list`, as discussed below, and slicing is not supported.

A `dict` is defined as a comma-separated list of key : value mappings between curly braces.


```python
ages = {
    'Jay-Z': 52,          # and counting
    'Emanuel Macron': 44  # and counting
}
print(ages)
```


### Getting a single element (indexing)

If you want to get an elements from a `dict`, you do this by specifying a `key`.


```python
age_jayz = ages['Jay-Z']
print(f'Jay-Z is {age_jayz} years old')
```

Alternatively, you can use `dict.get()`, which allows you to specify a default value in case the key is not in the `dict`.

```python
age_depp = ages.get('Johnny Depp', 'unknown')
print(f'Johnny Depp is {age_depp} years old')
```

<div class="exercise" id="exercise_dict" markdown="1">
#### Mini exercise

Define a `dict` of the three [largest cities in the world](https://en.wikipedia.org/wiki/List_of_largest_cities#List), where keys are names and values are population numbers in millions of inhabitants (e.g. 37 for Tokyo). Next, ask the user to enter the name of a city. If the city name is part of the `dict`, print out the population in the following format: 'The population of X is Y million inhabitants'. If the city name is not part of the `dict`, fall back to using 'unknown' for the population value.

When running the code, enter 'Tokyo' to solve the exercise.

<textarea class="code"></textarea>
<div hidden class="solution_output">The population of Tokyo is 30 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 31 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 32 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 33 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 34 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 35 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 36 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 37 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 38 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 39 million inhabitants</div>
<div hidden class="solution_output">The population of Tokyo is 40 million inhabitants</div>
</div>


## tuple: an ordered, immutable collection of elements

The `tuple` is very similar to a `list`. The main difference between the two types is that a `tuple` is *immutable*, which means that a `tuple` cannot be changed after it has been defined; in other words, there are no functions such as `tuple.append()`, `tuple.pop()`, etc. However, you can concatenate two `tuple`s using the `+` operator, in which case you get a new `tuple` that contains the elements of both of the concatenated `tuple`s.

A `tuple` supports indexing, slicing, `len()` and `in`, as described above for `list`s.

A `tuple` is defined as a comma-separated list of values, optionally surrounded by parentheses.


```python
fibonacci = 1, 1, 2, 3, 5
# Parentheses are optional unless they are required to avoid ambiguity
fibonacci = (1, 1, 2, 3, 5)
```


<div class="exercise" id="exercise_tuple" markdown="1">
#### Mini exercise

Create one `tuple` that contains the first five numbers of the fibonacci series. Create another `tuple` that contains the first five prime numbers. Concatenate the two `tuple`s and print out the result.

<textarea class="code"></textarea>
<div hidden class="solution_output">(1, 1, 2, 3, 5, 1, 3, 5, 7, 11)</div>
<div hidden class="solution_output">(1, 3, 5, 7, 11, 1, 1, 2, 3, 5)</div>
</div>

## set: an unordered, mutable collection of unique elements

The `set` is a somewhat unusual type, which you will rarely use unless you're doing mathematical computations. A `set` corresponds to a mathematical set as specified in [set theory](https://en.wikipedia.org/wiki/Set_theory).

A `set` supports `len()` and `in`, as described above for `list`s. However, a `set` does not support indexing or slicing.

A `set` is defined as a comma-separated list of values surrounded by curly braces.

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
```

A characteristic feature of `set`s is that each element can occur at most once (duplicates are ignored):

```python
print({'a', 'e'} == {'a', 'a', 'e', 'e'})
```

The `set` also supports standard operations from set theory:

- The union (`|`) of two sets contains all elements that occur in either or both of the sets
- The intersection (`&`) of two sets contains all elements that occur in both sets

```python
vowels_1 = {'a', 'e', 'i'}
vowels_2 = {'i', 'o', 'u'}
print('Union: {0}'.format(vowels_1 | vowels_2))
print('Intersection: {0}'.format(vowels_1 & vowels_2))
```

For more information, see:

- <https://docs.python.org/3.6/library/stdtypes.html?highlight=set#set>


<div class="exercise" id="exercise_set" markdown="1">
#### Mini exercise

Create one `set` that contains the first five numbers of the fibonacci series. Create another `set` that contains the first five prime numbers. Print out all numbers that occur in both sets (i.e. the intersection).

<textarea class="code"></textarea>
<div hidden class="solution_output">{1, 3, 5}</div>
</div>

## Review exercises

<div class='exercise no-progress' id='exercise_fibonacci' markdown=1>

### Fibonacci

%-- include: exercises/basic/iterables-1.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:iterables%-solution-1) to see one solution!

<textarea class="code height300"></textarea>

</div>

<div class='exercise no-progress' id='exercise_artists' markdown=1>

### Best-selling artists

%-- include: exercises/basic/iterables-2.md --%

This exercise is not checked automatically, because there are several possible solutions. Click [here](%url:iterables%-solution-2) to see one solution!

<textarea class="code height300"></textarea>

</div>
